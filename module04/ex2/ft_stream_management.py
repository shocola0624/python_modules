#!/usr/bin/env python3

import sys


def communication_system() -> None:
    """Prints messages via appropriate streams.

    Collects archivist identification and status information,
    then demonstrate proper channel separation by routing different message
    types to their appropriate streams.
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    arc_id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")
    print()

    print("{[}STANDARD{]} Archive status from "
          f"{arc_id}: {status}", file=sys.stdout)
    print("{[}ALERT{]} System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("{[}STANDARD{]} Data transmission complete", file=sys.stdout)

    print()
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    communication_system()
