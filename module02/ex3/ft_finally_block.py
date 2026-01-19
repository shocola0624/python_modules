#!/usr/bin/env python3

def water_plants(plant_list: list) -> None:
    """Opens watering system and goes through each plant.

    Args:
        plant_list (list): A list of plants
    """
    try:
        print("Opening watering system")
        for plant in plant_list:
            msg = "Watering " + plant
            print(msg)
        print("Watering completed successfully!")
    except TypeError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Demonstrates water_plants."""
    list1 = ["tomato", "lettuce", "carrots"]
    list2 = ["tomato", None]

    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(list1)
    print()
    print("Testing with error...")
    water_plants(list2)
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
