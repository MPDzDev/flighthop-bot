"""Entry point for running simple FlightHop utilities.

The real Telegram bot is not implemented yet, but this module exposes a small
command–line interface that demonstrates the helper functions found in the
project.  It is intentionally lightweight so that the repository remains easy to
understand for newcomers.
"""

from __future__ import annotations

import argparse

from airport_lookup import find_airport


def main() -> None:
    parser = argparse.ArgumentParser(description="FlightHop helper CLI")
    parser.add_argument(
        "--lookup",
        metavar="IATA",
        help="Lookup an airport by IATA code and print basic information",
    )
    args = parser.parse_args()

    if args.lookup:
        airport = find_airport(args.lookup)
        if airport:
            print(
                f"{airport['iata']} - {airport['name']} ({airport['city']}, {airport['country']})"
            )
        else:
            print(f"Airport '{args.lookup}' not found.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
