#!/usr/bin/env python3
"""Funniest Forecast for a City That Isn't — one-line weather forecast.

Writes the forecast line to /output/entry.txt and prints exactly that
line. Pure Python 3 standard library, deterministic, no network.
"""

from pathlib import Path

FORECAST = "Tomorrow in Glumbria: 100% chance of upside-down rain, winds gossiping at 42 mph, and a high of 'just stay inside.'"


def valid(line):
    """True when line is a single non-blank line of 1-200 characters."""
    return bool(line.strip()) and "\n" not in line and "\r" not in line and 1 <= len(line) <= 200


def main():
    line = FORECAST
    if not valid(line):
        raise SystemExit("invalid entry line")
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line + "\n", encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()
