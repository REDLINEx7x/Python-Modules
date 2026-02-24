class GardenError(Exception):
    """Base class for exceptions in this garden module."""
    pass


class PlantError(GardenError):
    """Exception raised for errors in the planting process."""
    pass


class WaterError(GardenError):
    """Exception raised for errors related to water levels or irrigation."""
    pass


def checking(task: str) -> None:
    """
    Checks the status of a specific garden task
    and raises the appropriate error.

    Args:
        task: The name of the garden task to check.
    """
    if task == "plant":
        raise PlantError("The tomato plant is wilting!")
    elif task == "water":
        raise WaterError(" Not enough water in the tank!")
    else:
        raise GardenError("Unknown garden task")


def testing_garden_error() -> None:
    """
    Demonstrates the functionality of custom garden exceptions by
    running through several error-prone scenarios.
    """
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        checking("plant")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    print("Testing WaterError...\n")
    try:
        checking("water")
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    tasks = ["plant", "water",]
    print("Testing catching all garden errors...\n")
    for i in tasks:
        try:
            checking(i)
        except GardenError as error:
            print(f"Caught a garden error: {error}")
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    testing_garden_error()
