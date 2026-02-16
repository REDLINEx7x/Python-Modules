


class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def increas_height(self, amount=1):
        self.height += amount
        print(f"{self.name} grew {amount}cm")
        def description(self):
                return f"{self.name} {self.height}cm"
    def plant_score(self):
        return self.height

class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.blooms = True
    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")
    def description(self):
        if self.blooms:
            return f"{self.name} {self.height}cm {self.color} is blooming"
        else:
            return f"{self.name} {self.height}cm {self.color} not blooming"

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color,prize_points):
        super().__init__(name, height, age, color)
        self.prize_points = prize_points
    def plant_score(self):
        return self.height + self.prize_points
    def description(self):
        base_info = super().description()
        return f"{base_info}, Prize points: {self.prize_points}"

class GardenManager:
    gardens_count  = 0
    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        GardenManager.gardens_count += 1
        self.total_growth = 0
    @classmethod
    def create_garden_network(cls, owners):
        new_gardens = []
        for name in owners:
            manager = cls(name)
            new_gardens.append(manager)
        return(new_gardens)
    def add_plant(self, plant):
        self.plants.append(plant)
    def grow_all(self):
        for plant in self.plants:
            plant.increas_hight(1)
        self.total_growth += 1

    class GardenStats:
        sum_total = 0
        @staticmethod
        def sum_scores(plant_list):
            for plant in plant_list:
                sum_total = plant.plant_score()
            return sum_total
    def report(self):
        print(f"=== {self.name}'s Garden Report ===")
        for plant in self.plants:
            print(f"{plant.description()}")

