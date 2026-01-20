#!/usr/bin/env python3

import sys


def command_quest() -> None:
    """Reads command-line arguments from `sys.argv` and prints."""
    print("=== Command Quest ===")

    av = sys.argv

    av_len = len(av)
    if av_len == 1:
        print("No arguments provided!")

    print(f"Program name: {av[0]}")
    if av_len > 1:
        print(f"Arguments received: {av_len-1}")

    i = 1
    for arg in av[1:]:
        print(f"Argument {i}: {arg}")
        i += 1

    print(f"Total arguments: {av_len}")


if __name__ == "__main__":
    command_quest()
