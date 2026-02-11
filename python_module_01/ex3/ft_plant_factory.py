class plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
         return f"{self.name} ({self.height}cm, {self.age} days)"
factory_data = [("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120),
    ("labobo", 20, 2000)
    ]
plants = []
print("=== Plant Factory Output ===")
i = 0
for name, height, age in factory_data:
    plants.append(plant(name, height, age))
    print(f"Created: {plants[i].get_info()}")
    i = i + 1
print ()
print ("Total plants created:", i)

