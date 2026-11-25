#!/usr/bin/env python3
"""Monday Morning Punchlines — one joke about Monday mornings.

Writes the entry joke to /output/entry.txt, where the harness reads it.
The gate allows 1–200 characters, so the program checks the length
before writing anything.
"""

from pathlib import Path

# The joke below is exactly 144 characters, well inside the 200-char gate.
JOKE = "I filed a formal complaint with the calendar about Monday mornings. It was denied. The calendar is corrupt, and Monday is its favorite employee."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke must be 1-200 chars, got {len(text)}"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
