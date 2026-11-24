#!/usr/bin/env python3
"""Say What Actually Broke — make.fun entry.

Writes one single-line software error message to /output/entry.txt.
The line names the real failure in plain words (the database is down),
tells the reader what to do next (try again in a few minutes), and
carries one funny image a reader can repeat to a colleague — while
staying shippable in a real product's error dialog.

Deterministic: the same bytes are written on every run.
"""

import os
import sys

ENTRY = (
    "The database is down. Your data is safe, but the server holding it "
    "has stopped answering its phone. Please try again in a few minutes."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate_entry(text: str) -> None:
    """Enforce the competition gate: UTF-8 text, 1-200 chars, one line,
    not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    # Must be encodable as UTF-8.
    text.encode("utf-8")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line (no newline characters)")


def main() -> int:
    validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # newline="" so no platform newline translation; write exactly one line.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
