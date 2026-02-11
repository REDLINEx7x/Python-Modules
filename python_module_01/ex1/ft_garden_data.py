
print("=== Garden Plant Registry ===")

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

Plant1 = Plant("Rose", "25cm", "30 days old")
Plant2 = Plant("Sunflower", "80cm", "45 days old")
Plant3 = Plant("Cactus", "15cm", "120 days old")

plants = [Plant1, Plant2, Plant3]

for i in range(3):
    print(plants[i].name,": ",plants[i].height,", ", plants[i].age, sep = "")
