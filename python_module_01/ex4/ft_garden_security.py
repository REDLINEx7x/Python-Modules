
class SecurePlant:

    def __init__(self, name, height, age):
        self.name = name
        self.__height = 0
        self.__age = 0

    #def get_info(self):
    #        return f"{self.name} ({self.__height}cm, {self.__age} days)"

    def set_height(self, current_height):
        if current_height >= 0:
            self.__height = current_height
            print( f"Height updated: {current_height}cm [OK]")
        else:
            print (f"Invalid operation attempted: height {current_height}cm [REJECTED]")
            print("Security: Negative age rejected")
    def get_height(self):
            return self.__height

    def set_age(self, current_age):
        if current_age >= 0:
            self.__age = current_age
            print(f"Age updated: {current_age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {current_age}days [REJECTED]")
            print("Security: Negative age rejected")
    def get_age(self):
        return self.__age

print("=== Garden Security System ===")
plant = SecurePlant("Rose", 0, 0)
#print(f"Current plant:{plant.get_info()}")
print("Plant created:" ,plant.name)
plant.set_height(25)
plant.set_age(30)
print()
plant.set_height(-3)
print()
print(f"Current plant: {plant.name} ({plant.get_height()}cm, {plant.get_age()} days)")
