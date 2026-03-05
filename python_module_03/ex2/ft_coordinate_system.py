import math
import sys


def tuple_handling(cord: str) -> tuple[int, int, int] | None:
    cord_list = cord.split(",")
    try:
        list_num = [int(value) for value in cord_list]
        if len(list_num) != 3:
            raise ValueError
        return tuple(list_num)

    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(f"Error details - Type: ValueError, Args: {error.args}")
        return None


def main() -> None:

    print("=== Game Coordinate System ===\n")

    tp0 = (0, 0, 0)
    tp1 = (10, 20, 5)
    print(f"Position created: {tp1}")
    distance = float(math.sqrt(tp1[0]**2 + tp1[1]**2 + tp1[2]**2))
    print(f"Distance between {tp0} and {tp1}: {distance:.2f}")
    print()

    """ Parsing coordinate string from command line or default
    """
    if len(sys.argv) == 1:
        coordinates = "3,4,0"
    else:
        coordinates = sys.argv[1]

    print(f"Parsing coordinates: \"{coordinates}\"")
    tp2 = tuple_handling(coordinates)

    if tp2 is not None:
        print(f"Parsed position: {tp2}")
        distance = float(math.sqrt(tp2[0]**2 + tp2[1]**2 + tp2[2]**2))
        print(f"Distance between {tp0} and {tp2}: {distance:.2f}")
    print()

    if len(sys.argv) == 1:
        invalid_cord = "abc,def,ghi"
        print(f"Parsing invalid coordinates: \"{invalid_cord}\"")
        tuple_handling(invalid_cord)
        print()

    print("Unpacking demonstration:")
    if tp2 is not None:
        x, y, z = tp2
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
    else:
        print("Cannot unpack coordinates: parsed position is None")


if __name__ == "__main__":
    main()
