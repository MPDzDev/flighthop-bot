"""Simple Telegram bot implementation for the FlightHop MVP."""

from __future__ import annotations

import json
import logging
from pathlib import Path

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from airport_lookup import find_airport
from game_state import GameState, load_state, save_state
from message_utils import (
    format_correct_guess,
    format_incorrect_guess,
    format_daily_challenge,
)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


DATA_PATH = Path(__file__).resolve().parent
ROUTES_PATH = DATA_PATH / "routes.json"
CONFIG_PATH = DATA_PATH / "config.json"


# Load routes once at startup.
with open(ROUTES_PATH, "r", encoding="utf-8") as f:
    ROUTES = json.load(f)


with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    CONFIG = json.load(f)


TELEGRAM_TOKEN = CONFIG.get("TELEGRAM_TOKEN")


def get_map_link(lat: float, lon: float) -> str:
    return f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}&zoom=10"


def get_current_destination(state: GameState) -> dict | None:
    if 0 <= state.current_leg < len(ROUTES):
        return ROUTES[state.current_leg]["to"]
    return None


async def start_journey(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    group_id = update.effective_chat.id
    state = load_state(group_id)
    if state.current_leg > 0:
        await update.message.reply_text("Journey already started!")
        return

    dest = get_current_destination(state)
    if not dest:
        await update.message.reply_text("No route data available.")
        return

    map_link = get_map_link(dest["lat"], dest["lon"])
    await update.message.reply_text(format_daily_challenge(map_link))
    save_state(state)


async def hint(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    group_id = update.effective_chat.id
    state = load_state(group_id)
    dest = get_current_destination(state)
    if not dest:
        await update.message.reply_text("No current flight.")
        return
    map_link = get_map_link(dest["lat"], dest["lon"])
    await update.message.reply_text(format_daily_challenge(map_link))


async def handle_guess(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text.strip()
    if len(text) != 3:
        return

    group_id = update.effective_chat.id
    state = load_state(group_id)
    dest = get_current_destination(state)
    if not dest:
        return

    guess = text.upper()
    if guess == dest["iata"].upper():
        airport = find_airport(dest["iata"])
        flag = ""
        if airport:
            country = airport.get("country", "").replace(" ", "+")
            flag = f"\U0001F30E"  # globe emoji as placeholder
        await update.message.reply_text(
            format_correct_guess(dest["iata"], dest["name"], flag)
        )
        state.current_leg += 1
        state.guesses.clear()
        save_state(state)
        await update.message.reply_text("✈️ Your next flight will be ready tomorrow.")
    else:
        await update.message.reply_text(format_incorrect_guess(guess))
        state.record_guess(guess)
        save_state(state)


async def next_flight(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    group_id = update.effective_chat.id
    state = load_state(group_id)
    dest = get_current_destination(state)
    if dest:
        await update.message.reply_text("Today's flight has not been completed yet.")
        return

    dest = get_current_destination(state)
    if not dest:
        await update.message.reply_text("No further flights configured.")
        return

    map_link = get_map_link(dest["lat"], dest["lon"])
    await update.message.reply_text(format_daily_challenge(map_link))
    save_state(state)


def main() -> None:
    if not TELEGRAM_TOKEN:
        raise SystemExit("TELEGRAM_TOKEN is not configured")

    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start_journey", start_journey))
    application.add_handler(CommandHandler("next_flight", next_flight))
    application.add_handler(CommandHandler("hint", hint))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_guess))

    application.run_polling()


if __name__ == "__main__":
    main()
