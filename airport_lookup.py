"""Airport lookup utilities for FlightHop.

This module loads airport information from ``airports.json`` and exposes helper
functions for looking up airports by their IATA code.  Only a very small data
set is bundled with the repository but the utility functions are written so
that the data file can easily be expanded.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Optional


# The repository currently stores ``airports.json`` in the project root.  Using
# ``Path(__file__).parent`` keeps the path working even if the module is moved
# into a package later on.
DATA_PATH = Path(__file__).resolve().parent / "airports.json"


def load_airports() -> list:
    """Load the list of airports from :data:`DATA_PATH`."""
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        # In development the file might be missing; return an empty list so the
        # caller can handle the situation gracefully.
        return []


# Cache of airports keyed by IATA code.  ``load_airports`` is relatively cheap
# but looking up airports repeatedly benefits from using a dictionary.
_AIRPORT_CACHE: Dict[str, Dict] | None = None


def _ensure_cache() -> None:
    global _AIRPORT_CACHE
    if _AIRPORT_CACHE is None:
        _AIRPORT_CACHE = {a["iata"].upper(): a for a in load_airports()}


def find_airport(iata: str) -> Optional[Dict]:
    """Return airport information for ``iata`` or ``None`` if not found."""

    _ensure_cache()
    assert _AIRPORT_CACHE is not None  # for type checkers
    return _AIRPORT_CACHE.get(iata.upper())


def get_airport_name(iata: str) -> Optional[str]:
    """Convenience wrapper returning only the airport name."""

    airport = find_airport(iata)
    if airport:
        return airport.get("name")
    return None

