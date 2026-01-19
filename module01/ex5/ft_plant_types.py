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


class Flower(Plant):
    """Represents a flower in your garden.

    In addition to Plant attributes, it has:
        color (str): Color of the flower
        blooming (bool): Whether the flower is blooming or not
    """

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initializes Flower.

        Args:
            - name
            - height
            - age
            - color
        """
        super().__init__(name, height, age)
        self.color = color
        self.blooming = False

    def bloom(self) -> None:
        """Blooms!"""
        self.blooming = True

    def get_info(self) -> None:
        """Shows current data of the flower."""
        print(f"{self.name} (Flower):",
              f"{self.height}cm, {self.age} days, {self.color} color")
        if (self.blooming):
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} is not blooming")


class Tree(Plant):
    """Represents a tree in your garden.

    In addition to Plant attributes, it has:
        trunk_diameter (int): Diameter of the tree trunk
        shade_area (int): Area covered by tree shade
    """

    def __init__(self, name: str, height: int,
                 age: int, trunk_diameter: int) -> None:
        """Initializes Tree.

        Args:
            - name
            - height
            - age
            - trunk_diameter
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_area = 0

    def produce_shade(self) -> None:
        """Sets shade_area."""
        self.shade_area = 78

    def get_info(self) -> None:
        """Shows current data of the tree."""
        print(f"{self.name} (Tree):",
              f"{self.height}cm, {self.age} days,",
              f"{self.trunk_diameter}cm diameter")
        print(f"{self.name} provides",
              f"{self.shade_area} square meters of shade")


class Vegetable(Plant):
    """Represents a vegetable in your garden.

    In addition to Plant attributes, it has:
        harvest_season (str): The season when the vegetable is harvested
        nutritional_value (str): The nutritional value of the vegetable
    """

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """Initializes Vegetable.

        Args:
            - name
            - height
            - age
            - nutritional_value
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> None:
        """Shows current data of the vegetable."""
        print(f"{self.name} (Vegetable):",
              f"{self.height}cm, {self.age} days,",
              f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")


def main() -> None:
    """Test code."""
    rose = Flower("Rose", 25, 30, "red")
    rose.bloom()
    oak = Tree("Oak", 500, 1825, 50)
    oak.produce_shade()
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    plants = [rose, oak, tomato]

    print("=== Garden Plant Types ===")
    for plant in plants:
        print()
        plant.get_info()


if __name__ == "__main__":
    main()
