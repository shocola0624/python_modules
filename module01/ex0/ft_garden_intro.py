#!/usr/bin/env python3

def ft_garden_intro(name: str, height: int, age: int) -> None:
    """Displays information about a plant in your garden.

    Args:
        name (str): Name
        height (int): Height in centimeters
        age (int): Age in days
    """
    print("=== Welcome to My Garden ===")
    print(f"Plant : {name}")
    print(f"Height : {height}cm")
    print(f"Age : {age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro("Rose", 25, 30)
