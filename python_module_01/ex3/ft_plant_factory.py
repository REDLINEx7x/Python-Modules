"""Simple plant factory demo
(create plants from tuples and print a summary).
"""


class Plant:
    """Small data holder for a plant."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Store plant fields."""
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """Return a one-line description."""
        return f"{self.name} ({self.height}cm, {self.age} days)"


factory_data = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120),
]
"""Seed data: (name, height_cm, age_days)."""

plants = []
"""Created Plant objects."""

print("=== Plant Factory Output ===")
i = 0
for name, height, age in factory_data:
    """Create each Plant and print it."""
    plants.append(Plant(name, height, age))
    print(f"Created: {plants[i].get_info()}")
    i = i + 1

print()
print("Total plants created:", i)
