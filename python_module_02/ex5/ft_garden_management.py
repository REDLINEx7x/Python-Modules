class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

class GardenManager:
    def __init__(self):
        self.plants = []
        self.tank = 40

    def add_plants(self, name, water, sun):
        if name == "":
            raise PlantError("Plant name cannot be empty!")

        for plant in self.plants:
            if plant['name'] == name:
                raise GardenError("plant name is already exist")

        self.plants.append({
            "name": name,
            "water": water,
            "sun": sun
        })
        print(f"Added {name} successfully")

    def water_plants(self):
        try:
            for plant in self.plants:
                if self.tank < 10:
                    raise GardenError("Not enough water in tank")

                self.tank -= 20
                print(f"Watering {plant['name']} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self):
        for plant in self.plants:
            name = plant['name']
            water_level = plant['water']
            s = plant['sun']

            if water_level > 10:
                raise PlantError(f"Error checking {name}: Water level {water_level} is too high (max 10)")
            print(f"{name}: healthy (water: {water_level}, sun: {s})")
    #def recovery(self):
    #    try:
    #        self.water_plants()
    #    except GardenError as error:
    #        print(f"Caught GardenError: {error}")
    #    finally:
    #        self.tank = 40
    #        print("System recovered and continuing...")

def test_garden_management():

    manager = GardenManager()
    print("=== Garden Management System ===")
    try:
        print("Adding plants to garden...")
        manager.add_plants("tomato", 5, 8)
        manager.add_plants("lettuce", 15, 5)
        manager.add_plants("", 5, 5)
    except PlantError as error:
        print(f"Error adding plant:{error}")
    print()
    try:
        print("Watering plants...")
        print("Opening watering system.")
        manager.water_plants()
        print()
    except WaterError as error:
        print(f"Error watering plants: {error}")
    print()
    try:
        print("Checking plant health...")
        manager.check_plant_health()
    except GardenError as error:
        print({error})
    print()
    print("Testing error recovery...")
    try:
        manager.water_plants()
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    finally:
        print("System recovered and continuing...")
    print("Garden management system test complete!")

if __name__ == "__main__":
    test_garden_management()
