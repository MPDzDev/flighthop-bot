"""
Game state utilities for FlightHop.

This module should define functions and classes to manage the state of each
Telegram group playing the FlightHop game. State includes current leg index,
correct guesses, and last played timestamps.
"""

# TODO: Implement state management functions

class GameState:
    def __init__(self, group_id: int):
        self.group_id = group_id
        self.current_leg = 0
        self.guesses = []
        self.last_played = None

    def to_dict(self) -> dict:
        return {
            "group_id": self.group_id,
            "current_leg": self.current_leg,
            "guesses": self.guesses,
            "last_played": self.last_played,
        }
