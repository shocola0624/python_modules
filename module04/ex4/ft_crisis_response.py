#!/usr/bin/env python3

def print_response(arc: str) -> None:
    """
    Read and display the contents of a file with structured status messages.

    This function attempts to open the file specified by `arc` in read mode.
    - If the file exists and is readable, its contents are printed with a
      success message.
    - If the file does not exist, a FileNotFoundError is caught and a
      corresponding error message is shown.
    - If access is denied, a PermissionError is caught and a security
      warning message is shown.
    """
    try:
        with open(arc, "r") as f:
            data = f.read()
            print(f"ROUTINE ACCESS: Attempting access to '{arc}'...\n"
                  f"SUCCESS: Archive recovered - ''{data}''\n"
                  "STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{arc}'...\n"
              "RESPONSE: Archive not found in storage matrix\n"
              "STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{arc}'...\n"
              "RESPONSE: Security protocols deny access\n"
              "STATUS: Crisis handled, security maintained\n")


def crisis_response_system() -> None:
    """
    Implements a crisis handler function for archive operations.
    The system must manage different types of archive access failures
    gracefully using failsafe protocols combined with
    the 'with statement' to prevent data corruption during errors.
    """
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    print_response("lost_archive.txt")
    print_response("classified_vault.txt")
    print_response("standard_archive.txt")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    crisis_response_system()
