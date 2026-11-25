"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one sentence recalling a childhood memory to /output/entry.txt.
The sentence is 184 characters long, one sentence, within the 1-280 gate.
"""

from pathlib import Path

LINE = "My grandmother kept my broken toy car on her windowsill for twenty years, and when I finally asked why, she said it was the only thing I ever brought her that I did not ask her to fix."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
