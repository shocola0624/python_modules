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

    def show(self) -> None:
        """Shows attributes of the plant."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    """Test code"""
    plants = []
    plants.append(Plant("Rose", 25, 30))
    plants.append(Plant("Sunflower", 80, 45))
    plants.append(Plant("Cactus", 15, 120))
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.show()


if __name__ == "__main__":
    main()
