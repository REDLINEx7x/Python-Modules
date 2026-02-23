"""Plant type models and sample usage for a garden."""


class Plant:
    """Base class representing a plant with common attributes."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a plant."""
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """Return formatted information about the plant."""
        # Only print attributes every plant has
        return (
            f"{self.name} ({self.__class__.__name__}): "
            f"{self.height}cm, {self.age} days"
        )


class Flower(Plant):
    """A flowering plant with a color attribute."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a flower."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        """Return a bloom status message."""
        return f"{self.name} is blooming beautifully!\n"

    def get_flower_info(self) -> str:
        """Return formatted information specific to a flower."""
        common_info = self.get_info()
        return f"{common_info}, {self.color} color"


class Tree(Plant):
    """A tree with a trunk diameter attribute."""

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int,
    ) -> None:
        """Initialize a tree."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> str:
        """Return a message describing the shade area."""
        shade_area = 3.14 * ((self.height / 100) ** 2)
        return (
            f"{self.name} provides {shade_area} square meters of shade"
            "\n"
        )

    def get_tree_info(self) -> str:
        """Return formatted information specific to a tree."""
        common_info = self.get_info()
        return f"{common_info}, {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    """A vegetable with harvest season and nutritional value."""

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        """Initialize a vegetable."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season

        self.nutritional_value = nutritional_value

    def get_vegetable_info(self) -> str:
        """Return formatted information specific to a vegetable."""
        common_info = self.get_info()
        return (
            f"{common_info}, {self.harvest_season} harvest\n"
            f"{self.name} is rich in {self.nutritional_value}"
        )


flowers = [
    Flower("Rose", 25, 30, "red"),
    Flower("Sunflower", 20, 25, "yellow"),
]

trees = [
    Tree("Oak", 500, 1825, 50),
    Tree("Pine", 180, 300, 25),
]

vegetables = [
    Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
    Vegetable("Carrot", 10, 60, "Spring", "Vitamin A"),
]

print("=== Garden Plant Types ===", end="\n\n")
i = 0
print(f"{flowers[i].get_flower_info()}")
print(f"{flowers[i].bloom()}")
print(f"{trees[i].get_tree_info()}")
print(f"{trees[i].produce_shade()}")
print(f"{vegetables[i].get_vegetable_info()}")
