class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.type = "regular"
    def increase_height(self, amount=1):
        self.height += amount
    def description(self):
        return f"{self.name} {self.height}cm"
    def plant_score(self):
        return self.height
class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.blooms = True
        self.type = "flowering"
    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")
    def plant_score(self):
        score = self.height
        if self.blooms:
            score += 15
        return score
    def description(self):
        if self.blooms:
            return f"{self.name} {self.height}cm {self.color} (blooming)"
        else:
            return f"{self.name} {self.height}cm {self.color} (not blooming)"

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, prize_points):
        super().__init__(name, height, age, color)
        self.prize_points = prize_points
        self.type = "prize flowers"
    def plant_score(self):
        score = self.height + self.prize_points
        if self.blooms:
            score += 15
        return score
    def description(self):
        base_info = super().description()
        return f"{base_info}, Prize points: {self.prize_points}"

class GardenManager:
    all_gardens  = []
    gardens_count  = 0
    def __init__(self, owner):
        GardenManager.all_gardens.append(self)
        self.owner = owner
        self.plants = []
        GardenManager.gardens_count += 1
        self.total_growth = 0
        self.plants_count = 0
    @classmethod
    def create_garden_network(cls, owners)-> list:
        new_gardens = []
        for name in owners:
            is_found = False
            for i in range(GardenManager.gardens_count):
                if name == GardenManager.all_gardens[i].owner:
                    is_found = True
                    break
            if is_found == False:
                manager = cls(name)
                new_gardens.append(manager)
        return(new_gardens)
    def add_plant(self, plant):
        self.plants.append(plant)
        self.plants_count += 1
        print(f"Added {plant.name} to {self.owner}'s garden")
    def grow_all(self):
        print(f"{self.owner} is helping all plants grow...")
        for i in range(self.plants_count):
            current_plant = self.plants[i]
            current_plant.increase_height(1)
            self.total_growth += 1
            print(f"{current_plant.name} grew 1cm")

    class GardenStats:
        @staticmethod
        def sum_scores(plant_list):
            sum_total = 0
            for plant in plant_list:
                sum_total += plant.plant_score()
            return sum_total
    def report(self):
        regular_count = 0
        flower_count = 0
        prize_count = 0
        height_is_valid = True
        print(f"=== {self.owner}'s Garden Report ===")
        print(f"Plants in garden:")
        for i in range(self.plants_count):
            current_plant = self.plants[i]
            print(f"{current_plant.description()}")
            if(current_plant.type == "regular"):
                regular_count += 1
            elif (current_plant.type == "flowering"):
                flower_count += 1
            elif(current_plant.type == "prize flowers"):
                prize_count += 1
            if(current_plant.height < 0):
                height_is_valid = False
        print(f"plants added: {self.plants_count}, Total growth: {self.total_growth}")
        print(f"Plant types :  {regular_count} regular, {flower_count} flowering, {prize_count} prize flowers")
        print(f"\nHeight validation test: {height_is_valid}")
    @classmethod
    def collecting_score(cls):
        output = "Garden scores - "
        for i in range(GardenManager.gardens_count):
            current_garden = GardenManager.all_gardens[i]
            score = GardenManager.GardenStats.sum_scores(current_garden.plants)
            if i < GardenManager.gardens_count - 1:
                output += f"{current_garden.owner}: {score}, "
            else:
                output += f"{current_garden.owner}: {score}"
        print(output)
        print(f"Total gardens managed: {GardenManager.gardens_count}")

owners = GardenManager.create_garden_network(["Alice", "Bob", "Alice", "Bob"])
alice = owners[0]
bob = owners[1]

plant1 = FloweringPlant("Rose", 25, 20, "red")
plant2 = PrizeFlower("Sunflower", 50, 30, "yellow", 10)
plant3 = Plant("Oak Tree", 100, 50)

alice.add_plant(plant1)
alice.add_plant(plant2)
alice.add_plant(plant3)
alice.grow_all()

alice.report()
plant4 = Plant("Cactus", 32, 40)
plant5 = FloweringPlant("Lavender", 15, 30, "purple")
plant6 = PrizeFlower("Tulip", 15, 30, "pink", 19)
bob.add_plant(plant4)
bob.add_plant(plant5)
bob.add_plant(plant5)
GardenManager.collecting_score()
