#!/usr/bin/env python3
"""Funniest Forecast for a City That Isn't — one-line weather forecast."""

import os

ENTRY = "Tomorrow in Glumbria: 100% chance of upside-down rain, winds gossiping at 42 mph, and a high of 'just stay inside.'"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
