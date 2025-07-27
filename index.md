# FlightHop Bot

FlightHop is a Telegram group game for learning airport codes, geography, and the travel ecosystem through real-world flight routes. The bot simulates a global journey by presenting one daily flight leg. Each day, players see a map pin for an airport and guess the 3-letter IATA code of the destination. When a guess is correct, the next leg unlocks on the following day.

## Group Chat Mode

FlightHop runs in Telegram group chats. It listens for guesses and messages from any group member and responds naturally in conversation.

### Group Behavior

- Only one challenge per day per group
- Everyone can guess, but only the correct code counts
- Minimal bot messages to avoid clutter
- Friendly tone, emoji-rich, travel-themed replies

## Learning Objectives

- Master global airport codes via repetition and guessing
- Learn geography through map-based deduction
- Build spatial memory by seeing airport locations
- Encourage short, daily learning habits
- Introduce the travel ecosystem in a kid-friendly way

## Key Features

- **✈️ Daily Flight Challenge** – One new airport pin per day
- **🗺️ Map-Based Clue** – Zoomable OpenStreetMap link to locate the airport
- **🔤 IATA Guessing** – Wordle-style guessing (3-letter airport codes, up to 6 tries)
- **✅ Correct Response** – Confirmation, airport name, country flag
- **📚 Wikipedia Link** – Direct link to Wikipedia search for further learning
- **👩‍✈️ Stewardess Tip** – Short tip to build cabin crew awareness
- **🕓 Progression** – Follows real airline route chains (e.g., STN → DUB → AMS → …)
- **🗨️ Group Integration** – Natural replies, no spam, supports nickname mentions

## Example Game Flow

```
Bot: 🛫 FlightHop Challenge of the Day!
🌍 Where in the world are we today? Tap the map and guess the IATA code.

📍 https://www.openstreetmap.org/?mlat=53.4213&mlon=-6.2701&zoom=10

Niece: DUB  
Bot: ✅ Correct! You’ve landed at DUB (Dublin Airport) 🇮🇪  
🔗 Learn more: https://en.wikipedia.org/wiki/Special:Search?search=Dublin+Airport  
👩‍✈️ Stewardess Tip: Smile warmly while passengers board—first impressions matter.  
✈️ Your next flight will be ready tomorrow.
```

## Tech Stack

| Layer | Tool |
|------|------|
| Language | Python |
| Telegram API | python-telegram-bot |
| Data Storage | TinyDB (JSON-based; upgradeable to SQLite/Postgres) |
| Map Service | OpenStreetMap static links (no API key needed) |
| Hosting | Free tiers on Replit, Railway, or Render |
| Data Source | Curated from OpenFlights |

## Data Format Example

The bot uses simple JSON files to describe flight routes. Here is an example:

```json
[
  {
    "from": "STN",
    "to": {
      "iata": "DUB",
      "name": "Dublin Airport",
      "lat": 53.4213,
      "lon": -6.2701
    }
  }
]
```

## Bot Command Overview

| Command | Use |
|---------|-----|
| `/start_journey` | Start the first leg (STN) |
| `/next_flight` | Proceed if the daily limit allows |
| `@BotName hint` | Resend today’s map link |
| `XXX` | Submit a three-letter IATA code guess |
| `/route` | See the current flight path |
| `/scoreboard` | See who guessed most correctly |

## Cost and Hosting

| Resource | Cost |
|---------|-----|
| Telegram Bot API | Free |
| Hosting (Replit/Railway/Render) | Free tiers available |
| OpenStreetMap | Free |
| Google Maps (optional backup) | Limited free tier (not required) |

For personal use with a niece or small family group, this bot costs approximately €0/month to run.

## Progression Logic

- Starts at a fixed hub: London Stansted (STN)
- Next destination chosen based on:
  - Most frequent real-world routes
  - European focus
  - Low-cost airline paths (Ryanair, EasyJet, Wizz)
- Linear journey: one path, one leg per day

## Directory Structure

```
flighthop/
├── bot.py
├── data/
│   ├── airports.json
│   ├── routes.json
│   └── state.json
├── utils/
│   ├── game_state.py
│   ├── airport_lookup.py
│   └── message_utils.py
├── config.json
├── requirements.txt
└── README.md
```

## Growth Ideas (Optional Features)

- **Custom Airline** – Players name their airline and see it in replies
- **Route Map** – Show the full path on a rendered map after five stops
- **Country Passport** – Flag stamp for each new country visited
- **Roleplay Mode** – Cabin scenarios: how would you respond?
- **Localized Wikipedia** – Option to open Wikipedia in Italian, Polish, etc.

## Target Audience

Age range: 10–99+

Plays via family Telegram group

Interested in geography, aviation, or stewardess life

iPhone and Android both supported

---

Stay tuned for updates and feel free to contribute by submitting pull requests or opening issues!
