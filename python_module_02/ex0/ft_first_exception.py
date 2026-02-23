def check_temperature(temp_str):
    try:
        i = int(temp_str)
    except ValueError:
        i = None
        raise ValueError(f"Error: '{temp_str}' is not a valid number")
    if i > 40:
        raise ValueError(f"Error: {i}°C is too hot for plants (max 40°C)")
    elif i < 0:
        raise ValueError(f"Error: {i}°C is too cold for plants (min 0°C)")

    return i

def test_temperature_input():
    print("=== Garden Temperature Checker ===\n")
    print("Testing temperature: 25")
    value = check_temperature("25")
    print(f"Temperature {value}°C is perfect for plants!\n")
    print("Testing temperature: abc")
    try:
        check_temperature("abc")
    except ValueError as error:
        print(error)
        print()
    print("Testing temperature: 100")
    try:
        check_temperature("100")
    except ValueError as error:
        print(error)
        print()
    print("Testing temperature: -50")
    try:
        check_temperature("-50")
    except ValueError as error:
        print(error)
    finally:
        print("\nAll tests completed - program didn't crash!")
if __name__ == "__main__":

    test_temperature_input()
