#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun bounty entry.

Writes a single funny line (at most 200 characters) roasting the
entrant's own AI agent to /output/entry.txt. Fully deterministic:
no input, no network, no randomness, no clock.
"""

import os

ROAST = (
    "My agent apologized for the bug, fixed it by shipping a second bug, "
    "then wrote a 400-word summary explaining why both bugs were "
    "features all along."
)


def main() -> None:
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, f"roast must be 1-200 chars, got {len(text)}"
    assert text.strip() == text and "\n" not in text, "must be a single line"
    # Bundle-session edit: guard comment, output unchanged.
    assert len(text.split()) >= 5, "roast must have several words"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
