"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one sentence recalling a childhood memory to /output/entry.txt.
The sentence is 200 characters long, one sentence, within the 1-280 gate.
"""

from pathlib import Path

LINE = "The school bell rang at three and the whole street ran home barefoot, and I only realised this year that the fastest boy in our gang grew up to be the postman who still waves at every child he passes."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
