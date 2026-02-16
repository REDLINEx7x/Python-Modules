


class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def increas_height(self, amount=1):
        self.height += amount
        print(f"{self.name} grew {amount}cm")
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

class GardenManager:
    gardens_count  = 0
    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        GardenManager.gardens_count += 1

    @classmethod
    def create_garden_network(cls, owners):
        new_gardens = []
        for name in owners:
            manager = cls(name)
            new_gardens.append(manager)
        return(new_gardens)
    def add_plant(self, plant):
        self.plants.append(plant)
    class GardenStats:
        @staticmethod
        def sum_scores(plant_list):
            return
