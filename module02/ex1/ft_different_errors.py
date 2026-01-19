#!/usr/bin/env python3

def garden_operations(error_type: str) -> None:
    """Demonstrates some common errors.

    Args:
        error_type (str): Error to be caused
    """
    if error_type == "ValueError":
        _ = int("abc")

    elif error_type == "ZeroDivisionError":
        _ = 42 / 0

    elif error_type == "FileNotFoundError":
        open("missing.txt")

    elif error_type == "KeyError":
        data = {"missing_plant": 42}
        _ = data["missing\\_plant"]

    elif error_type[:8] == "multiple":
        _ = 42 / 0 + int("abc")


def test_error_types() -> None:
    """Shows each type of error happening."""
    error_types = ["ValueError",
                   "ZeroDivisionError",
                   "FileNotFoundError",
                   "KeyError",
                   "multiple errors together"]
    error_msgs = {
        "ValueError": "invalid literal for int()",
        "ZeroDivisionError": "division by zero",
        "FileNotFoundError": "No such file 'missing.txt'",
        "KeyError": "'missing\\_plant'"
    }

    print("=== Garden Error Types Demo ===\n")
    for error_type in error_types:
        print(f"Testing {error_type}...")
        try:
            garden_operations(error_type)
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            if error_type[:8] == "multiple":
                print("Caught an error, but program continues!")
            else:
                print(f"Caught {error_type}: ", end="")
                msg = error_msgs[error_type]
                print(msg)
            print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
