def check_plant_health(
    plant_name: str, water_level: int, sunlight_hours: int
) -> str:
    """
    Validates plant health and returns a success message if valid.

    Args:
        plant_name: The name of the plant species.
        water_level: An integer between 1 and 10.
        sunlight_hours: An integer between 2 and 12.

    Returns:
        str: A message confirming the plant is healthy.

    Raises:
        ValueError: If the plant name is empty or parameters are out of bounds.
    """
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")

    if water_level < 1:
        raise ValueError(
            f"Error: Water level {water_level} is too low (min 1)"
        )
    elif water_level > 10:
        raise ValueError(
            f"Error: Water level {water_level} is too high (max 10)"
        )

    if sunlight_hours < 2:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours} is too low (min 2)"
        )
    elif sunlight_hours > 12:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours} is too high (max 12)"
        )

    return f"Plant {plant_name} is healthy!\n"


def test_plant_checks() -> None:
    """
    Runs a series of test cases for check_plant_health to verify logic.
    """
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    try:
        result = check_plant_health("tomato", 2, 4)
        print(result)
    except ValueError as error:
        print(f"{error}\n")

    print("Testing empty plant name...")
    try:
        check_plant_health(None, 3, 2)
    except ValueError as error:
        print(f"{error}\n")

    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 2)
    except ValueError as error:
        print(f"{error}\n")

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 3, 0)
    except ValueError as error:
        print(f"{error}\n")

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
