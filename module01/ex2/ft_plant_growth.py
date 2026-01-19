#!/usr/bin/env python3

class Plant:
    """Represents a plant in your garden.

    Attributes:
        name (str): Name
        height (int): Height in centimeters
        days (int): Age in days
        start_height (int): Height given as an argument
    """

    def __init__(self, name: str, height: int, days: int) -> None:
        """Initializes the Plant.

        Args:
            - name
            - height
            - days
        """
        self.name = name
        self.height = height
        self.days = days
        self.start_height = height

    def grow(self) -> None:
        """Increases height by one centimeter."""
        self.height += 1

    def age(self) -> None:
        """Increases age by one day."""
        self.days += 1

    def get_info(self) -> None:
        """Shows attributes of the plant."""
        print(f"{self.name}: {self.height}cm, {self.days} days old")


def main() -> None:
    """Test code."""
    rose = Plant("Rose", 25, 30)

    print("=== Day1 ===")
    rose.get_info()

    print("=== Day 7 ===")
    i = 0
    while (i < 6):
        rose.grow()
        rose.age()
        i += 1
    rose.get_info()
    growth = rose.height - rose.start_height
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    main()
