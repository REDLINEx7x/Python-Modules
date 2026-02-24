def water_plants(plant_list: list) -> None:
    """
    Iterates through a list of plants and simulates a watering process.

    Checks each plant against the available garden plants. If a plant
    is not found in the dictionary, an error message is displayed.

    Args:
        plant_list (list): A list of strings representing plant names.
    """
    garden_plants = {"tomato": None, "lettuce": None, "carrots": None}
    try:
        print("Opening watering system")
        for plant in plant_list:
            garden_plants[plant]
            print(f"Watering {plant}")
    except KeyError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """
    Runs test cases for the water_plants function, including
    successful scenarios and error handling.
    """
    print("=== Garden Watering System ===")
    plants = ["tomato", "lettuce", "carrots",]
    invalid_plants = ["tomato", None]
    print("Testing normal watering...")
    water_plants(plants)
    print("watering completed successfully!\n")
    print("Testing with error...")
    water_plants(invalid_plants)
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
