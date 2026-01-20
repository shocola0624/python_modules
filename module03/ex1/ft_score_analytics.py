#!/usr/bin/env python3

import sys


def score_analytics() -> None:
    """Calculates scores.

    Accepts player scores from command-line and make a list to store.
    Shows total, high/low score, average and score range.
    """
    print("=== Player Score Analytics ===")

    scores = []
    av = sys.argv
    if len(av) == 1:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    # make list
    for arg in av[1:]:
        try:
            scores.append(int(arg))
        except ValueError as e:
            print(e)
            return

    # calculate total / high / low / average scores
    total = 0
    high = scores[0]
    low = scores[0]
    for score in scores:
        total += score
        if high < score:
            high = score
        if low > score:
            low = score
    average = total / len(scores)

    # print
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {high-low}")


if __name__ == "__main__":
    score_analytics()
