"""
Message formatting utilities for FlightHop.

This module should include helper functions to format bot messages, such as
formatting guesses, progress notifications, and stewardess tips.
"""

# TODO: Implement message formatting functions

def format_correct_guess(iata: str, airport_name: str, country_flag: str) -> str:
    return f"✅ Correct! You’ve landed at {iata} ({airport_name}) {country_flag}"
