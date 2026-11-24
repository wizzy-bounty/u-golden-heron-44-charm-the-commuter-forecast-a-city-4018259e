#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (at most 140 characters) for the
fictional city of Upwick to /output/entry.txt.

Upwick is a city that does not exist, where the rain falls upwards:
the forecast keeps the rhythm of a real broadcast ("Today in ..."),
names the place, gives it weather, and turns on the commuter's own
morning — hold the umbrella underneath you, the bus is on time, and
your shoes are soaked from below.
"""

import os

FORECAST = (
    "Today in Upwick: rain falling upwards, so hold your umbrella "
    "underneath you \u2014 the 8:15 bus is on time, your shoes are "
    "soaked from below."
)


def main() -> None:
    out_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(FORECAST)


if __name__ == "__main__":
    main()
