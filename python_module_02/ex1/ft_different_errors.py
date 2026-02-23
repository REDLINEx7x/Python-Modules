def garden_operation(test):

    if test == "bad data":
        num = int("abc")
    elif test == "divide by zero":
        num = 100 / 0
    elif test == "file not found":
        file = open("missing.txt", 'r')
    elif test == ("key error"):
        garden = {"Rose": 1, "sunflower": 2,}
        print(garden["missing\\_plant"])


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    try:
       garden_operation("bad data")
    except ValueError as error:
        print(f"Caught ValueError:  invalid literal for int()\n")
    print("Testing ZeroDivisionError...")
    try:
        garden_operation("divide by zero")
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: division by zero\n")
    print("Testing FileNotFoundError..")
    try:
        garden_operation("file not found")
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file 'missing.txt'\n")
    print("Testing KeyError...")
    try:
        garden_operation("key error")
    except KeyError as error:
        print(f"Caught KeyError: 'missing\\_plant'\n")
    try:
        garden_operation("bad data")
        garden_operation("divide by zero")
        garden_operation("file not found")
    except Exception:
        print("Caught an error, but program continues!\n")
    finally:
        print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
