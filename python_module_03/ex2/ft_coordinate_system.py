import math

def tuple_handling(cord: str) -> tuple | None:
    """
    Parses a string of comma-separated coordinates into a tuple of integers.

    Args:
        cord (str): The coordinate string to parse (e.g., "3,4,0").

    Returns:
        tuple | None: A tuple of integers if successful, or None if parsing fails.
    """
    #dist = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)
    cord_list = cord.split(",")
    list_num = []
    try:
        for i in cord_list:
            list_num += [(int(i))]
        return tuple(list_num)
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(f"Error details - Type: ValueError, Args: {error.args}")
        return None


if __name__=="__main__":
    """
    Main execution block for the 3D Coordinate System demonstration.
    """
    print("=== Game Coordinate System ===\n")

    # Initial coordinate setup and distance calculation
    tp0 = (0, 0, 0)
    tp1 = (-39, -23, -11)
    print(f"Position created: {tp1}")

    # Distance calculation using the 3D Euclidean formula
    #
    distance = float(math.sqrt(tp1[0]**2 + tp1[1]**2 + tp1[2]**2))
    print(f"Distance between {tp0} and {tp1}: {distance:.2f}")
    print()

    # Parsing valid coordinate string
    coordinates = "-39, -23, -11"
    print(f"Parsing coordinates: \"{coordinates}\"")
    tp2 = tuple_handling(coordinates)
    print(f"Parsed position: {tp2}")

    distance = float(math.sqrt(tp2[0]**2 + tp2[1]**2 + tp2[2]**2))
    print(f"Distance between {tp0} and {tp2}: {distance:.2f}")
    print()

    # Parsing invalid coordinate string to demonstrate error handling
    invalid_cord = "abc,def,ghi"
    print(f"Parsing invalid coordinates: {invalid_cord}")
    tuple_handling(invalid_cord)
    print()

    # Demonstration of tuple unpacking
    print("Unpacking demonstration:")
    if tp2:
        x, y, z = tp2
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
