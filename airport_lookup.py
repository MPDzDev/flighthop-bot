"""
Airport lookup utilities for FlightHop.

This module should load the airports.json data and provide functions to find
airport information by IATA code, including coordinates, city, and country.
"""

# TODO: Implement airport lookup functions

import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "airports.json"

def load_airports() -> list:
    try:
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
