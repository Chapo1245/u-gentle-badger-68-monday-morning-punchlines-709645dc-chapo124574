"""Monday Morning Punchlines — make.fun entry.

Writes one fresh joke about Monday mornings (144 characters) to
/output/entry.txt. Deterministic: no input, no network, no randomness.
"""

import os

JOKE = (
    "I filed a formal complaint with the calendar about Monday mornings. "
    "It was denied. The calendar is corrupt, and Monday is its favorite employee."
)


def main() -> None:
    assert 1 <= len(JOKE) <= 200, f"joke must be 1-200 chars, got {len(JOKE)}"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
