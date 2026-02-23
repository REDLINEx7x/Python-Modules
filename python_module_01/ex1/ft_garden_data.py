"""Print a small registry of garden plants and their basic attributes."""


class Plant:
    """Simple container for a plant's name, height, and age."""

    def __init__(self, name: str, height: str, age: str) -> None:
        """Initialize the plant."""
        self.name = name
        self.height = height
        self.age = age


Plant1 = Plant("Rose", "25cm", "30 days old")
Plant2 = Plant("Sunflower", "80cm", "45 days old")
Plant3 = Plant("Cactus", "15cm", "120 days old")

plants = [Plant1, Plant2, Plant3]
print("=== Garden Plant Registry ===")
for i in range(3):
    print(plants[i].name, ": ", plants[i].height, ", ", plants[i].age, sep="")
