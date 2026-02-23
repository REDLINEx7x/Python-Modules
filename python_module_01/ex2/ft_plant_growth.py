"""Simple weekly plant growth simulation."""


class Plant:
    """Plant with name, height, and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the plant."""
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """Return a short description of the plant."""
        return f"{self.name}: {self.height} cm, {self.age} days old"

    def grow(self) -> None:
        """Increase height by 1 cm."""
        self.height = self.height + 1

    def aging(self) -> None:
        """Increase age by 1 day."""
        self.age = self.age + 1


plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Sunflower", 80, 45)
plant3 = Plant("Cactus", 15, 120)
plants_list = [plant1, plant2, plant3]

execute_plant = plant1

for day in range(1, 8):
    if day == 1:
        start = execute_plant.height
        print(f"=== Day {day} ===")
        print(execute_plant.get_info())
        for plant in plants_list:
            plant.grow()
            plant.aging()
    elif day == 7:
        print(f"=== Day {day} ===")
        print(execute_plant.get_info())
    else:
        for plant in plants_list:
            plant.grow()
            plant.aging()

total = execute_plant.height - start
print(f"Growth this week: +{total} cm")
