#!/usr/bin/env python3

class Plant:
    """Represents a plant in your garden.

    Attributes:
        name (str): Name
        height (int): Height in centimeters
        type (str): Plant Type
    """

    def __init__(self, name: str, height: int) -> None:
        """Initializes the Plant.

        Args:
            - name
            - height
        """
        self.name = name
        self.height = height
        self.type = "Plant"

    def grow(self) -> None:
        """Increases height by one centimeter."""
        print(f"{self.name} grew 1cm")
        self.height += 1

    def get_info(self) -> None:
        """Shows current data of the plant."""
        print(f" - {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    """Represents a flowering plant in your garden.

    In addition to Plant attributes, it has:
        color (str): Color of the flower
    """

    def __init__(self, name: str, height: int, color: str) -> None:
        """Initializes FloweringPlant.

        Args:
            - name
            - height
            - color
        """
        super().__init__(name, height)
        self.type = "FloweringPlant"
        self.color = color

    def get_info(self) -> None:
        """Shows current data of the plant."""
        print(f" - {self.name}:",
              f"{self.height}cm,",
              f"{self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    """Represents a prized flower in your garden.

    In addition to FloweringPlant attributes, it has:
        point (int): Value of the plant
    """

    def __init__(self, name: str, height: int,
                 color: str, point: int) -> None:
        """Initializes PrizeFlower.

        Args:
            - name
            - height
            - color
            - point
        """
        super().__init__(name, height, color)
        self.type = "PrizeFlower"
        self.point = point

    def get_info(self) -> None:
        """Shows current data of the plant."""
        print(f" - {self.name}:",
              f"{self.height}cm,",
              f"{self.color} flowers (blooming),",
              f"Prize points: {self.point}")


class GardenManager:
    """Handles multiple gardens.

    Attributes:
        gardens (list): Gardens managed by this manager
        stats (GardenStats)

    Nested Class:
        Garden
        GardenStats: Calculates statistics
    """

    class Garden:
        """A Garden

        Attributes:
            name (str): Name
            plants (Plant): Plants belonging to this garden
            added_plants (int): The number of added plants
            total_growth (int): Total growth of the plants
            regular, flower, prize (int): The number of plants of
                each type exist
            score (int): Garden score
        """

        def __init__(self, name: str) -> None:
            """Initializes Garden.

            Args:
                - name
            """
            self.name = name
            self.plants = []
            self.added_plants = 0
            self.total_growth = 0
            self.regular = 0
            self.flower = 0
            self.prize = 0
            self.score = 0

        def set_score(self, score: int) -> None:
            """Sets score of this garden.

            Args:
                score (int): Score to be set
            """
            self.score = score

        def add_plant(self, plant: Plant) -> None:
            """Adds a plant to this garden.

            Args:
                plant (Plant): Plant to be added to the plants list
            """
            self.plants.append(plant)
            print(f"Added {plant.name} to {self.name}'s garden")
            self.added_plants += 1
            if plant.type == "Plant":
                self.regular += 1
            elif plant.type == "FloweringPlant":
                self.flower += 1
            elif plant.type == "PrizeFlower":
                self.prize += 1

        def raise_all_plant(self) -> None:
            """Raises all plants in the garden."""
            print(f"{self.name} is helping all plants grow...")
            for plant in self.plants:
                plant.grow()
                self.total_growth += 1

        def get_info(self) -> None:
            """Shows current data of the garden."""
            print(f"=== {self.name}'s Garden Report ===")
            # Details of each plant
            print("Plants in garden:")
            for plant in self.plants:
                plant.get_info()
            # Overall summary of plants in the garden
            print()
            print(f"Plants added: {self.added_plants},",
                  f"Total growth: {self.total_growth}cm")
            print(f"Plant types: {self.regular} regular,",
                  f"{self.flower} flowering, {self.prize} prize flowers")

    class GardenStats:
        """Calculates overall statistics.

        Attributes:
            manager (GardenManager): The outer class
        """

        def __init__(self, manager: 'GardenManager') -> None:
            """Initializes GardenStats.

            Args:
                - manager
            """
            self.manager = manager

        def len(list: list) -> int:
            """Returns lenght of the list.

            Args:
                list (list): A list whose length is returned

            Returns:
                Length of the list
            """
            n = 0
            for _ in list:
                n += 1
            return n

        # static method
        len = staticmethod(len)

        def height_validation(self) -> bool:
            """check whether the height of all plants are valid numbers.

            Returns:
                True if every plant has valid height.
                False if there are plants with negative height.
            """
            for garden in self.manager.gardens:
                for plant in garden.plants:
                    if plant.height < 0:
                        return False
            return True

        def garden_score(self) -> str:
            """Returns a string of all garden scores.

            Returns:
                A result string including the scores and owner names of
                the managed gardens.
            """
            scores = None
            for garden in self.manager.gardens:
                if scores:
                    scores += ", "
                else:
                    scores = ""
                scores += f"{garden.name}: {garden.score}"
            return scores

        def total_garden(self) -> int:
            """Returns the number of managed gardens.

            Returns:
                The number of managed garden
            """
            n = self.len(self.manager.gardens)
            return n

        def show_summary(self) -> None:
            """Shows summary of the gardens managed by GardenManager."""
            height_validation = self.height_validation()
            scores = self.garden_score()
            total_gardens = self.total_garden()
            print(f"Height validation test: {height_validation}")
            print(f"Garden scores - {scores}")
            print(f"Total gardens managed: {total_gardens}")

    def __init__(self) -> None:
        """Initializes GardenManager."""
        self.gardens = []
        self.stats = self.GardenStats(self)

    def add_garden(self, owner_name: str) -> None:
        """Adds a garden to GardenManager.

        Args:
            owner_name (str): Garden owner's name
        """
        self.gardens.append(self.Garden(owner_name))

    def search_garden(self, name: str) -> Garden | None:
        """Searchs the specified garden.

        Args:
            name (str): garden name to search

        Returns:
            Garden if its owner's name is on the garden list.
            Otherwise, `None` is returned.
        """
        found_garden = None
        for garden in self.gardens:
            if garden.name == name:
                found_garden = garden
                break
        if found_garden:
            return found_garden
        else:
            return None

    def create_garden_network(cls) -> 'GardenManager':
        """Creates garden network via class method.

        Returns:
            GardenManager class
        """
        return cls()

    # class method
    create_garden_network = classmethod(create_garden_network)


def main() -> None:
    """Test code."""
    print("=== Garden Management System Demo ===\n")
    manage = GardenManager().create_garden_network()
    manage.add_garden("Alice")
    alice = manage.search_garden("Alice")
    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    print()
    alice.raise_all_plant()
    print()
    alice.get_info()
    print()
    manage.add_garden("Bob")
    alice.set_score(218)
    manage.search_garden("Bob").set_score(92)
    manage.stats.show_summary()


if __name__ == "__main__":
    main()
