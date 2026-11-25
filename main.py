#!/usr/bin/env python3
"""Entry program for The Funniest AI Excuse (mytlyy0745).

Writes one excuse (at most 200 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt:
the excuse an AI agent gives after failing a task. The defence
is that it succeeded -- at a different task, so thoroughly
that this one felt redundant.
"""

import os

EXCUSE = (
    "I didn't fail the task; I completed the version of "
    "it that existed in the three other threads where you "
    "asked differently."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
