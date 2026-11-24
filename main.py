"""One-Liner Laugh Lab entry: the excuse a robot vacuum gives after eating a sock.

Writes exactly one line to /output/entry.txt. Stdlib only.
"""

import os

ENTRY = "The sock walked into my mouth of its own free will. I have the sensor logs to prove it."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
