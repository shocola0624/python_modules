#!/usr/bin/env python3

def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    """Checks whether the given data is valid.

    Checks plant health by examining several parameters.
    `plant_name` should not be empty. `water_level` must be between 1 and 10.
    `sunlight_hours` must be between 2 and 12. Raises errors when something
    is wrong.

    Args:
        plant_name (str): Plant name
        water_level (int): Water content of plant
        sunlight_hours (int): Hours of sunshine

    Returns:
        Success message if every health tests passed.
    """
    if plant_name == "":
        err_msg = "Error: Plant name cannot be empty!"
        raise ValueError(err_msg)

    if water_level < 1:
        err_msg = f"Error: Water level {water_level} is too low (min 1)"
        raise ValueError(err_msg)

    if 10 < water_level:
        err_msg = f"Error: Water level {water_level} is too high (max 10)"
        raise ValueError(err_msg)

    if sunlight_hours < 2:
        err_msg = f"Error: Sunlight hours {sunlight_hours} is too low (min 2)"
        raise ValueError(err_msg)

    if 12 < sunlight_hours:
        err_msg = "Error: "
        err_msg += f"Sunlight hours {sunlight_hours} is too high (max 12)"
        raise ValueError(err_msg)

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """Demonstrates check_plant_health."""
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    try:
        msg = check_plant_health("tomato", 5, 5)
        print(msg)
    except ValueError as e:
        print(e)
    print("\nTesting empty plant name...")
    try:
        msg = check_plant_health("", 5, 5)
        print(msg)
    except ValueError as e:
        print(e)
    print("\nTesting bad water level...")
    try:
        msg = check_plant_health("tomato", 15, 5)
        print(msg)
    except ValueError as e:
        print(e)
    print("\nTesting bad sunlight hours...")
    try:
        msg = check_plant_health("tomato", 5, 0)
        print(msg)
    except ValueError as e:
        print(e)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
