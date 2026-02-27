"""Module for managing a smart garden system with error handling."""


class GardenError(Exception):
    """Base class for garden-related exceptions."""

    pass


class PlantError(GardenError):
    """Exception raised for plant-related errors."""

    pass


class WaterError(GardenError):
    """Exception raised for water-related errors."""

    pass


class GardenManager:
    """Manages plants and watering resources in a garden."""

    def __init__(self) -> None:
        """Initialize the garden manager."""
        self.plants = []
        self.tank = 40

    def add_plants(self, name: str, water, sun) -> None:
        """
        Add a new plant to the system after validating inputs.

        Args:
            name: The name of the plant.
            water: The required water level.
            sun: The required sunlight level.

        Raises:
            PlantError: If name is empty, duplicate, or levels aren't integers.
        """
        if name == "":
            raise PlantError("Plant name cannot be empty!")
        for plant in self.plants:
            if plant['name'] == name:
                raise PlantError("Plant name already exists")
        try:
            water_val = int(water)
            sun_val = int(sun)
        except (ValueError, TypeError):
            raise PlantError("Water and sun levels must be valid integers!")

        self.plants.append({
            "name": name,
            "water": water_val,
            "sun": sun_val
        })
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        """
        Water all plants in the garden using the tank resource.

        Raises:
            WaterError: If the water tank level is below 20.
        """
        for plant in self.plants:
            if self.tank < 20:
                raise WaterError("Not enough water in tank")

            self.tank -= 20
            print(f"Watering {plant['name']} - success")

    def check_plant_health(self) -> None:
        """Check health of all plants and report issues without stopping."""
        for plant in self.plants:
            try:
                name = plant['name']
                water_level = plant['water']
                sunlight = plant['sun']
                if water_level > 10:
                    raise PlantError(
                        f"Error checking {name}: Water level {water_level} "
                        f"is too high (max 10)"
                    )
                print(f"{name}: healthy (water: {water_level}, "
                      f"sun: {sunlight})")
            except PlantError as error:
                print(error)


def test_garden_management() -> None:
    """Demonstrate garden management system functionality and recovery."""
    manager = GardenManager()
    print("=== Garden Management System ===")
    try:
        print("Adding plants to garden...")
        manager.add_plants("tomato", 5, 8)
        manager.add_plants("lettuce", 15, 5)
        manager.add_plants("", 5, 5)
    except PlantError as error:
        print(f"Error adding plant: {error}")
    print()

    try:
        print("Watering plants...")
        print("Opening watering system")
        manager.water_plants()
    except WaterError as error:
        print(f"Error watering plants: {error}")
    finally:
        print("Closing watering system (cleanup)")
    print()

    try:
        print("Checking plant health...")
        manager.check_plant_health()
    except GardenError as error:
        print(error)
    print()

    print("Testing error recovery...")
    try:
        manager.water_plants()
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    finally:
        print("System recovered and continuing...\n")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
