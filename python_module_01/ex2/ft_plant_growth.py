class plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
         return f"{self.name}: {self.height} cm, {self.age} days old"
    def grow(self):
         self.height = self.height + 1

    def aging(self):
        self.age = self.age + 1

plant1 = plant("Rose", 25, 30)
plant2 = plant("Sunflower", 80, 45)
plant3 = plant("Cactus", 15, 120)
plants_list = [plant1, plant2, plant3]

excute_plant = plant1

for day in range(1,8):
    if(day == 1):
        start = excute_plant.height
        print(f"=== Day {day} ===")
        print(excute_plant.get_info())
        for plant in plants_list:
            plant.grow()
            plant.aging()
    elif(day == 7):
        print(f"=== Day {day} ===")
        print(excute_plant.get_info())

    else:
        for plant in plants_list:
            plant.grow()
            plant.aging()
total = excute_plant.height - start
print(f"Growth this week: +{total} cm")
            #print(excute_plant.get_info())
