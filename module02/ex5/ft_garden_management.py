#!/usr/bin/env python3


class GardenError(Exception):
    """A basic error for garden problems."""
    pass


class PlantError(GardenError):
    """For problems with plants."""
    pass


class WaterError(GardenError):
    """For problems with watering."""
    pass


class Plant:
    """Plant Class

    Atributes:
        name (str): Plant name
        water_level (int): Water content of plant
        sunlight_hours (int): Hours of sunshine
    """

    def __init__(self, name: str, water: int, sunlight: int) -> None:
        """Initializes the Plant.

        Args:
            name
            water_level
            sunlight_hours
        """
        self.name = name
        self.water_level = water
        self.sunlight_hours = sunlight


class GardenManager:
    """GardenManager Class

    Atributes:
        plants (list): A list of plants
        tank_error (bool): Whether the tank is broken
    """

    def __init__(self) -> None:
        """Initializes the GardenManager."""
        self.plants = []
        self.tank_error = True

    def add_plants(self, name: str, water: int, sunlight: int) -> None:
        """Adds the plant to the list.

        Args:
            name (str): Plant name
            water_level (int): Water content of plant
            sunlight_hours (int): Hours of sunshine
        """
        try:
            if name == "":
                msg = "Error adding plant: Plant name cannot be empty!"
                raise PlantError(msg)
            self.plants.append(Plant(name, water, sunlight))
            print(f"Added {name} successfully")
        except PlantError as e:
            print(e)

    def water_plants(self) -> None:
        """Opens watering system and goes through each plant."""
        try:
            print("Opening watering system")
            for plant in self.plants:
                if plant.name == "":
                    msg = "Error watering plant: Plant name cannot be empty!"
                    raise WaterError(msg)
                print(f"Watering {plant.name} - success")
                plant.water_level += 1
        except WaterError as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        """Checks if plants are healthy."""
        for plant in self.plants:
            try:
                if plant.name == "":
                    msg = f"Error checking {plant.name}: "
                    msg += "Plant name cannot be empty!"
                    raise PlantError(msg)
                if plant.water_level < 1:
                    msg = f"Error checking {plant.name}: Water level "
                    msg += f"{plant.water_level} is too low (min 1)"
                    raise PlantError(msg)
                if 10 < plant.water_level:
                    msg = f"Error checking {plant.name}: Water level "
                    msg += f"{plant.water_level} is too high (max 10)"
                    raise PlantError(msg)
                if plant.sunlight_hours < 2:
                    msg = f"Error checking {plant.name}: Sunlight hours "
                    msg += f"{plant.sunlight_hours} is too low (min 2)"
                    raise PlantError(msg)
                if 12 < plant.sunlight_hours:
                    msg = f"Error checking {plant.name}: Sunlight hours "
                    msg += f"{plant.sunlight_hours} is too high (max 12)"
                    raise PlantError(msg)
                print(f"{plant.name}: healthy (water: {plant.water_level},",
                      f"sun: {plant.sunlight_hours})")
            except PlantError as e:
                print(e)

    def error_recovery(self) -> None:
        """Error Recovery"""
        try:
            if self.tank_error:
                msg = "Caught GardenError: Not enough water in tank"
                raise GardenError(msg)
        except GardenError as e:
            print(e)
            print("System recovered and continuing...")
            self.tank_error = False


def test_management_system() -> None:
    """Demonstrates garden management system."""
    manager = GardenManager()
    print("=== Garden Management System ===\n")

    print("Adding plants to garden...")
    manager.add_plants("tomato", 4, 8)
    manager.add_plants("lettuce", 14, 10)
    manager.add_plants("", 10, 10)
    print()

    print("Watering plants...")
    manager.water_plants()
    print()

    print("Checking plant health...")
    manager.check_plant_health()
    print()

    print("Testing error recovery...")
    manager.error_recovery()
    print()

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_management_system()
