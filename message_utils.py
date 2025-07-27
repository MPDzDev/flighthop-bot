"""Helpers for formatting user-facing messages used by the bot."""

from __future__ import annotations


def format_correct_guess(iata: str, airport_name: str, country_flag: str) -> str:
    """Return a success message for a correct IATA guess."""

    return f"✅ Correct! You’ve landed at {iata} ({airport_name}) {country_flag}"


def format_incorrect_guess(iata: str) -> str:
    """Return a gentle message for an incorrect guess."""

    return f"❌ {iata.upper()} isn't the destination. Try again!"


def format_daily_challenge(map_link: str) -> str:
    """Return the daily challenge introduction with a map link."""

    lines = [
        "🛫 FlightHop Challenge of the Day!",
        "🌍 Where in the world are we today? Tap the map and guess the IATA code.",
        f"\n📍 {map_link}",
    ]
    return "\n".join(lines)

