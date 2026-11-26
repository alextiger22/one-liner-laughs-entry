#!/usr/bin/env python3
"""One-Liner Laughs.

make.fun entry for "One-Liner Laughs"
(u-coral-404-one-liner-laughs-aa872d41).

Prints the winning one-line joke (gauntlet Top 1, Alex's pick).
"""

JOKE = "I asked the GPS for the fastest route to success. It said 'recalculating' and has been silent for six years."


def main():
    # Read-back self-verification: the joke must be one single
    # line under 200 characters.
    lines = JOKE.splitlines()
    assert len(lines) == 1, "joke must be a single line"
    assert len(JOKE) <= 200, "joke must be under 200 characters"
    assert JOKE.strip(), "joke must not be empty"
    assert JOKE == JOKE.strip(), "joke must have no surrounding whitespace"
    assert JOKE.endswith("."), "joke must end with a full stop"
    print(JOKE)


if __name__ == "__main__":
    main()
