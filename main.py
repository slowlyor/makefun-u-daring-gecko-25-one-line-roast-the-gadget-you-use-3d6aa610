#!/usr/bin/env python3
"""Write one original one-line roast to /output/entry.txt.

Competition: u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610
("One-Line Roast: The Gadget You Use Every Day", make.fun).

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
not only whitespace. The program is deterministic, stdlib only,
and makes no network calls.
"""

import os

MAX_CHARS = 200  # gate: /output/entry.txt must be 1..200 characters

ROAST = (
    "My banking app texts me a six-digit code, then logs me out "
    "for taking too long to type the six-digit code it just sent."
)


def validate(text: str) -> None:
    """Fail loudly rather than ever writing an entry the gate refuses."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("roast is empty or only whitespace")
    if "\n" in stripped:
        raise ValueError("roast must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"roast is {len(text)} chars, over the 200 limit")


def main() -> None:
    validate(ROAST + "\n")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
