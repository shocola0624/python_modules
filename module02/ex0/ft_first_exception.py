#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int | None:
    """Checks if the temperature is reasonable for plants.

    Args:
        temp_str (str): A string of the temperature

    Return:
        The temperature if it's valid. Otherwise, `None` is returned
    """
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None

    if temp > 40:
        print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
        return None

    elif temp < 0:
        print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
        return None

    print(f"Temperature {temp_str}°C is perfect for plants!")
    return temp


def test_temperature_input() -> None:
    """Demonstrates check_temperature()."""
    print("=== Garden Temperature Checker ===\n")
    test = ["25", "abc", "100", "-50"]
    for temp_str in test:
        print(f"Testing temperature: {temp_str}\n")
        check_temperature(temp_str)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
