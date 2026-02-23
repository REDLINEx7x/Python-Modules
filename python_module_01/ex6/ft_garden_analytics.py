"""
ft_garden_analytics.py

A small garden management demo using basic OOP concepts:
- `Plant` as a base class
- `FloweringPlant` and `PrizeFlower` as specialized subclasses
- `GardenManager` to manage gardens and compute reports/scores
"""


class Plant:
    """A basic plant with a name, height (cm), and age.

    Attributes:
        name: Plant name.
        height: Plant height in centimeters.
        age: Plant age (units are user-defined; typically months/years).
        type: A simple string label used for reporting.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a regular plant."""
        self.name = name
        self.height = height
        self.age = age
        self.type = "regular"

    def increase_height(self, amount: int = 1) -> None:
        """Increase the plant height by `amount` centimeters."""
        self.height += amount

    def description(self) -> str:
        """Return a human-readable description of the plant."""
        return f"- {self.name}: {self.height}cm"

    def plant_score(self) -> int:
        """Return a score used for comparing plants (default: height)."""
        return self.height


class FloweringPlant(Plant):
    """A plant that can bloom and has a flower color.

    Adds:
        color: The flower color.
        blooms: Whether the plant is currently blooming.
        type: Set to "flowering" for reporting.
    """

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a flowering plant."""
        super().__init__(name, height, age)
        self.color = color
        self.blooms = True
        self.type = "flowering"

    def bloom(self) -> None:
        """Print a short message indicating the plant is blooming."""
        print(f"{self.name} is blooming beautifully!\n")

    def plant_score(self) -> int:
        """Compute the plant score.

        Base score is height. Adds a bloom bonus when `blooms` is True.
        """
        score = self.height
        if self.blooms:
            score += 15
        return score

    def description(self) -> str:
        """Return a description including flower color and bloom status."""
        if self.blooms:
            return (
                f"- {self.name}: {self.height}cm, {self.color} flowers "
                "(blooming)"
            )
        else:
            return (
                f"{self.name}: {self.height}cm, {self.color} flowers "
                "(not blooming)"
            )


class PrizeFlower(FloweringPlant):
    """A flowering plant that also contributes prize points to its score.

    Adds:
        prize_points: Extra points added to scoring.
        type: Set to "prize flowers" for reporting.
    """

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
        prize_points: int,
    ) -> None:
        """Initialize a prize flower."""
        super().__init__(name, height, age, color)
        self.prize_points = prize_points
        self.type = "prize flowers"

    def plant_score(self) -> int:
        """Compute the plant score including prize points and bloom bonus."""
        score = self.height + self.prize_points
        if self.blooms:
            score += 15
        return score

    def description(self) -> str:
        """Return a description including prize points."""
        base_info = super().description()
        return f"{base_info}, Prize points: {self.prize_points}"


class GardenManager:
    """Manage a garden for an owner and track plants, growth, and scoring.

    Class attributes:
        all_gardens: List of all GardenManager instances created.
        gardens_count: Number of gardens managed (mirrors len(all_gardens)).
    """

    all_gardens = []
    gardens_count = 0

    def __init__(self, owner: str) -> None:
        """Create a new garden manager for `owner` and register it globally."""
        GardenManager.all_gardens.append(self)
        self.owner = owner
        self.plants = []
        GardenManager.gardens_count += 1
        self.total_growth = 0
        self.plants_count = 0

    @classmethod
    def create_garden_network(cls, owners: list[str]) -> list["GardenManager"]:
        """
        Creates a network of GardenManager instances for owner names.

        This method ensures that no duplicate managers are created.
        It performs two levels of validation:
        1. Checks against the global registry (cls.all_gardens).
        2. Checks against the names processed in the current call.

        Args:
            owners (list[str]): A list of owner names to be registered.

        Returns:
            list[GardenManager]: A list containing the newly created
                GardenManager instances for unique owners.
        """
        new_gardens = []

        for name in owners:
            is_found = False

            for i in range(cls.gardens_count):
                if name == cls.all_gardens[i].owner:
                    is_found = True
                    break
            if not is_found:
                for g in new_gardens:
                    if name == g.owner:
                        is_found = True
                        break
            if not is_found:
                manager = cls(name)
                new_gardens.append(manager)

        return new_gardens

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to this garden and update the internal plant count."""
        self.plants.append(plant)
        self.plants_count += 1
        # print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        """Increase the height of every plant in the garden by 1 cm.

        Also increments `total_growth` for each 1 cm growth applied.
        """
        print(f"{self.owner} is helping all plants grow...")
        for i in range(self.plants_count):
            current_plant = self.plants[i]
            current_plant.increase_height(1)
            self.total_growth += 1
            print(f"{current_plant.name} grew 1cm")

    class GardenStats:
        """Utility container for garden-related scoring helpers."""

        @staticmethod
        def sum_scores(plant_list: "list[Plant]") -> int:
            """Sum the `plant_score()` of each plant in `plant_list`."""
            sum_total = 0
            for plant in plant_list:
                sum_total += plant.plant_score()
            return sum_total

    def report(self) -> None:
        """Print a report for this garden: plants,
            counts, growth, and checks.
        """
        regular_count = 0
        flower_count = 0
        prize_count = 0
        height_is_valid = True
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for i in range(self.plants_count):
            current_plant = self.plants[i]
            print(current_plant.description())
            if current_plant.type == "regular":
                regular_count += 1
            elif current_plant.type == "flowering":
                flower_count += 1
            elif current_plant.type == "prize flowers":
                prize_count += 1
            if current_plant.height < 0:
                height_is_valid = False
        print()
        print(
            f"Plants added: {self.plants_count}, "
            f"Total growth: {self.total_growth}cm"
        )
        print(
            "Plant types: "
            f"{regular_count} regular, {flower_count} flowering, "
            f"{prize_count} prize flowers"
        )
        print(f"\nHeight validation test: {height_is_valid}")

    @classmethod
    def collecting_score(cls) -> None:
        """Print scores for all managed gardens and the total garden count."""
        output = "Garden scores - "
        for i in range(cls.gardens_count):
            current_garden = cls.all_gardens[i]
            score = cls.GardenStats.sum_scores(current_garden.plants)
            if i < cls.gardens_count - 1:
                output += f"{current_garden.owner}: {score}, "
            else:
                output += f"{current_garden.owner}: {score}"
        print(output)
        print(f"Total gardens managed: {cls.gardens_count}")


owners = GardenManager.create_garden_network(["Alice", "Bob"])
alice = owners[0]
bob = owners[1]
print("=== Garden Management System Demo ===")
print()
plant1 = Plant("Oak Tree", 100, 50)
plant2 = FloweringPlant("Rose", 25, 20, "red")
plant3 = PrizeFlower("Sunflower", 50, 30, "yellow", 10)
plant4 = Plant("Cactus", 32, 40)
plant5 = FloweringPlant("Lavender", 15, 30, "purple")
plant6 = PrizeFlower("Tulip", 15, 30, "pink", 0)

alice.add_plant(plant1)
alice.add_plant(plant2)
alice.add_plant(plant3)
print(
    f"Added {plant1.name} to {alice.owner}'s "
    "garden"
)
print(
    f"Added {plant2.name} to {alice.owner}'s "
    "garden"
)
print(
    f"Added {plant3.name} to {alice.owner}'s "
    "garden\n"
)
bob.add_plant(plant4)
bob.add_plant(plant5)
bob.add_plant(plant6)
alice.grow_all()
print()
alice.report()
GardenManager.collecting_score()
