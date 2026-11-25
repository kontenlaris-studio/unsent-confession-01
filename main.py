#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — writes one unsent message to /output/entry.txt.

Two lines: a "To:" line, then the message itself. The confession is
never sent, and the reason is inside it: an unopened toolbox is a
son admitting, quietly, that he never learned how — so the message
stays a draft, and the toolbox stays a shrine.
"""
import os

ENTRY = (
    "To: Dad\n"
    "I still have the toolbox you gave me when I turned eighteen. "
    "I've never opened it because using it would mean admitting "
    "I never learned how.\n"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
