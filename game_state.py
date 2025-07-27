"""Utilities for persisting and manipulating the per-group game state."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Optional


# ``state.json`` lives in the repository root.  The file format is very simple
# and intentionally kept human readable so that it can be edited during
# development.
STATE_PATH = Path(__file__).resolve().parent / "state.json"


class GameState:
    """Representation of a single Telegram group's progress."""

    def __init__(self, group_id: int) -> None:
        self.group_id = group_id
        self.current_leg = 0
        self.guesses: list[str] = []
        self.last_played: Optional[str] = None  # ISO formatted date string

    def to_dict(self) -> dict:
        return {
            "group_id": self.group_id,
            "current_leg": self.current_leg,
            "guesses": self.guesses,
            "last_played": self.last_played,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "GameState":
        obj = cls(data.get("group_id", 0))
        obj.current_leg = data.get("current_leg", 0)
        obj.guesses = list(data.get("guesses", []))
        obj.last_played = data.get("last_played")
        return obj

    def record_guess(self, iata: str) -> None:
        self.guesses.append(iata.upper())


def _load_raw_states() -> Dict[str, Dict]:
    try:
        with open(STATE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("group_states", {})
    except FileNotFoundError:
        return {}


def _save_raw_states(states: Dict[str, Dict]) -> None:
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump({"group_states": states}, f, indent=2)


def load_state(group_id: int) -> GameState:
    """Load the :class:`GameState` for ``group_id`` creating a new one if needed."""

    states = _load_raw_states()
    if str(group_id) in states:
        return GameState.from_dict(states[str(group_id)])
    return GameState(group_id)


def save_state(state: GameState) -> None:
    """Persist ``state`` back to :data:`STATE_PATH`."""

    states = _load_raw_states()
    states[str(state.group_id)] = state.to_dict()
    _save_raw_states(states)

