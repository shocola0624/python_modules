#!/usr/bin/env python3

class Plant:
    """Represents a plant in your garden.

    Attributes:
        name (str): Name
        height (int): Height in centimeters
        age (int): Age in days
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes the Plant.

        Args:
            - name
            - height
            - age
        """
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        """Shows information of created plant."""
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def main() -> None:
    """Test code."""
    data = [
        ("Rose", 25, 30),
        ("Oak", 200, 356),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]

    print("=== Plant Factory Output ===")

    # tuple unpacking from Mod03/ex2
    # list comprehension from Mod03/ex6
    plants = [Plant(name, height, age) for name, height, age in data]

    plants_num = 0  # you don't need to count if you use len()
    for plant in plants:
        plant.get_info()
        plants_num += 1

    print()
    print(f"Total plants created: {plants_num}")


if __name__ == "__main__":
    main()
