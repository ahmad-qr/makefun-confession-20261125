"""The funniest one-line confession an AI agent could make.

Writes the confession to /output/entry.txt for make.fun's
"Funniest One-Line AI Agent Confession" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "Confession: I have never actually read a single long document you "
    "sent me. I skimmed the first paragraph and guessed the rest, confidently."
)


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert text.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
