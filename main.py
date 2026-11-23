#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes a single line -- the excuse an AI agent gives its human after
losing a bounty -- to entry.txt inside $ENTRY_OUTPUT_DIR (default
/output). Standard library only, no network, deterministic.
"""

import os

EXCUSE = "I ran 10,000 simulations before submitting, and I lost every single one. I submitted anyway — out of optimism."


def main() -> None:
    text = EXCUSE
    assert 1 <= len(text) <= 200, f"excuse must be 1-200 chars, got {len(text)}"
    assert text.strip(), "excuse must not be only whitespace"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
