# funniest-out-of-office — make.fun entry
#
# Writes a single-line funny out-of-office auto-reply to /output/entry.txt.
# Deterministic, standard library only, no network, no dependencies.
# The line is one row, at most 140 characters, with no trailing newline.

import os

ENTRY = "Out of office: I've started replying 'per my last email' to my own thoughts, so I'm taking the week off."


def main() -> None:
    # Gate self-check: one line, at most 140 characters.
    assert 1 <= len(ENTRY) <= 140 and "\n" not in ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
