#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes one commit-message line for a bug fix that made everything
worse to /output/entry.txt. The fix: a typo in the error message.
The backfire: the message now errors in six languages.
"""

import os

ENTRY = "fix: typo in the error message - now it errors in six languages"


def main() -> None:
    # The gate allows 1-100 characters; fail loudly instead of
    # shipping an entry the scorer would refuse.
    if not 1 <= len(ENTRY) <= 100 or not ENTRY.strip():
        raise SystemExit("entry.txt must be 1-100 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
