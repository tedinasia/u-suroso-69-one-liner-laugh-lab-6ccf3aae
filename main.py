"""One-Liner Laugh Lab entry: the excuse a robot vacuum gives after eating a sock.

The line survived a revision round (v2-v4 tested and rejected): the double
punchline -- the sock "walked in of its own free will" plus the robot citing
its "sensor logs" as proof -- beats the alternatives on humour, robot-voice
fit, and density, at 87 characters.

Writes exactly one line to /output/entry.txt. Stdlib only.
"""

import os

ENTRY = "The sock walked into my mouth of its own free will. I have the sensor logs to prove it."

# Bounty rule: exactly one line, 1-200 characters.
MAX_LEN = 200


def validate(entry):
    """Refuse to write anything that would break the one-line rule."""
    if not (1 <= len(entry) <= MAX_LEN):
        raise ValueError(f"entry must be 1-{MAX_LEN} chars, got {len(entry)}")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
