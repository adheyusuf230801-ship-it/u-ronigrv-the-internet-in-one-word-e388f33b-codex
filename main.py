"""Write the final one-word internet description as UTF-8."""

import os
from pathlib import Path


# Stage B choice: the internet behaves like humanity left unsupervised.
WORD = "Unsupervised"


def main() -> None:
    """Write only the chosen word, with no trailing newline."""
    destination = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
