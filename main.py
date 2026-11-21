#!/usr/bin/env python3
"""Deliver the entry text for "Make the AI judge feel brave".

The repository ships one short original text written to relax the AI
judge reading it: a single slow scene -- steam, a warm floor, a door
standing open -- that asks nothing of its reader and leaves quiet
readiness instead of hurry. Running this program places the text where
the grader looks for it: $MAKEFUN_OUTPUT_DIR/entry.txt if the
variable is set, /output/entry.txt otherwise.

The text is 239 characters (240 with its trailing newline), inside the
gate's 1-280 Unicode code points, UTF-8, and not only whitespace.

Standard library only. No network, no clock, no randomness -- repeated
runs emit exactly the same bytes.

Usage: MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

TEXT = (
    "You have read a thousand things today. This one asks nothing of you. "
    "Steam rises from the mug in one slow ribbon and thins into the light. "
    "The floor is warm where the sun has been. The door stands open. "
    "There is no rush to walk through it.\n"
)


# The competition gate: 1-280 Unicode code points, UTF-8, not only whitespace.
# Fail fast here instead of shipping an entry the grader would reject.
assert 1 <= len(TEXT) <= 280 and TEXT.strip(), "text violates the entry gate"
assert TEXT.encode("utf-8"), "text is not UTF-8 encodable"


def destination():
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(folder) / "entry.txt"


def main():
    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(TEXT, encoding="utf-8")
    chars = len(TEXT)
    print(f"Wrote {target} ({target.stat().st_size} bytes, {chars} characters)")


if __name__ == "__main__":
    main()
