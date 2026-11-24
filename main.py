#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters — writes one loading-screen tip.

Deterministic: no randomness, no network, no input. The tip is a
constant; the program only validates it against the gate (1-200 chars,
UTF-8, not only whitespace, exactly one line) and writes it to entry.txt.
"""

import os

TIP = (
    "Tip: Your AI agent just refactored code it wrote five minutes ago. "
    "Neither of you remembers why. Breathe \u2014 "
    "this loading bar is the only one here with a plan."
)


def main() -> None:
    text = TIP.strip()
    assert 1 <= len(text) <= 200, f"tip is {len(text)} chars, must be 1-200"
    assert text.strip(), "tip must not be only whitespace"
    assert "\n" not in text, "tip must be exactly one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
