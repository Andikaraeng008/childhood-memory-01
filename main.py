"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one sentence recalling a childhood memory to /output/entry.txt.
The sentence is about my grandfather's radio, which has played the same
station since 1987: the songs already know the way home, and he will not
confuse them. It is 184 characters long, one sentence, within the 1-280 gate.
"""

from pathlib import Path

LINE = "My grandfather's radio has played the same station since 1987, and when I asked him to change it once, he said the songs already knew the way home and he was not going to confuse them."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
