#!/usr/bin/env python3

class SecurePlant:
    """Represents a plant in your garden.

    Attributes:
        __name (str): Name
        __height (int): Height in centimeters
        __age (int): Age in days
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes the Plant.

        Args:
            - name
            - height
            - age
        """
        self.__name = name
        self.__height = height
        self.__age = age

    def set_height(self, new_height: int) -> None:
        """Modifies height in a safe way.

        Args:
            new_height (int): Height to be set
        """
        if (new_height < 0):
            print("Security : Negative height rejected")
            return
        self.__height = new_height

    def set_age(self, new_age: int) -> None:
        """Modifies age in a safe way.

        Args:
            new_age (int): Age to be set
        """
        if (new_age < 0):
            print("Security : Negative age rejected")
            return
        self.__age = new_age

    def get_height(self) -> int:
        """Only gets height.

        Returns:
            Current height of the plant.
        """
        return self.__height

    def get_age(self) -> int:
        """Only gets age.

        Returns:
            Current age of the plant."""
        return self.__age

    def get_info(self) -> None:
        """Shows current data of the plant."""
        print("Current plant:",
              f"{self.__name} ({self.__height}cm, {self.__age} days)")


def main() -> None:
    """Test code."""
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 0, 0)
    print("Plant created: Rose")
    rose.set_height(25)
    print("Height updated: 25cm [OK]")
    rose.set_age(30)
    print("Age updated: 30 days [OK]\n")
    rose.set_height(-5)
    print("Invalid operation attempted: height -5cm [REJECTED]\n")
    rose.get_info()


if __name__ == "__main__":
    main()
