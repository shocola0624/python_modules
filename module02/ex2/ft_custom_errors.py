#!/usr/bin/env python3

class GardenError(Exception):
    """A basic error for garden problems."""
    pass


class PlantError(GardenError):
    """For problems with plants."""
    pass


class WaterError(GardenError):
    """For problems with watering."""
    pass


def demo_custom_error(error_type: str) -> None:
    """Demonstrates specific custom error.

    Args:
        error_type (str): Custom error to be caused
    """
    print(f"Testing {error_type}...")

    # PlantError
    if error_type == "PlantError":
        try:
            err_msg = "Caught PlantError: The tomato plant is wilting!"
            raise PlantError(err_msg)
        except PlantError as e:
            print(e)

    # WaterError
    elif error_type == "WaterError":
        try:
            err_msg = "Caught WaterError: Not enough water in the tank!"
            raise WaterError(err_msg)
        except WaterError as e:
            print(e)

    # All Garden Errors
    else:
        try:
            msg1 = "Caught a garden error: The tomato plant is wilting!"
            msg2 = "Caught a garden error: Not enough water in the tank!"
            err_msg = msg1 + "\n" + msg2
            raise PlantError and WaterError(err_msg)
        except GardenError as e:
            print(e)


def test_custom_errors() -> None:
    """Demonstrates custom errors in order."""
    error_types = [
        "PlantError",
        "WaterError",
        "catching all garden errors"
    ]

    print("=== Custom Garden Errors Demo ===\n")

    for error_type in error_types:
        demo_custom_error(error_type)
        print()

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
