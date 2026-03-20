import math


def distance(tuple1: tuple[int, int, int],
             tuple2: tuple[int, int, int]) -> float:
    """
    Calculate the Euclidean distance between two 3D coordinate tuples.

    :param tuple1: The starting (x, y, z) coordinates.
    :param tuple2: The ending (x, y, z) coordinates.
    :return: The distance as a float.
    """
    """Additional comment: Tuples are a type of data that
    doesn't let you alter its content after its creation"""
    x1, y1, z1 = tuple1  # Separated by the 'unpacking' technique
    x2, y2, z2 = tuple2
    distance = math.sqrt(((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))
    return distance


def parsing_str_to_int(coor_str: str) -> tuple | None:
    """
    Convert a comma-separated string into a tuple of integers.

    :param coor_str: A string in 'x,y,z' format.
    :return: A tuple of three integers or None if parsing fails.
    """
    # split needs the separator char and returns the list separated
    coor_list = coor_str.split(",")
    cx0, cy0, cz0 = coor_list
    try:
        parse_coor = (int(cx0), int(cy0), int(cz0))
    except ValueError as e:
        # Print the special char \" as "
        print(f"Parsing invalid coordinates: \"{coor_str}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")
        # prints the arguments of the error
        return
    return parse_coor


def coordinates_test() -> None:
    """Run a demonstration of coordinate parsing and distance calculation."""
    print("=== Game Coordinate System ===\n")

    pos = (10, 20, 5)  # structure to declare a tuple: var = (x, y, z)
    pos0 = (0, 0, 0)
    dis = distance(pos0, pos)
    print(f"Position created: {pos}")
    # The dis:.2f allows you to choose the decimals to show (2 in here)
    print(f"Distance between {pos0} and {pos}: {dis:.2f}\n")

    coor_str = "3,4,0"
    tuple_coor = parsing_str_to_int(coor_str)
    if not tuple_coor:
        return
    else:
        print(f"Parsing coodinates: \"{coor_str}\"")
        print(f"Parsed position: {tuple_coor}")
        dis = distance((0, 0, 0), tuple_coor)
        print(f"Distance between (0, 0, 0) and {tuple_coor}: {dis:.1f}\n")
        # only a decimal

    # Bad input, tuple_coor will be 'None'
    coor_str = "abc,def,ghi"
    tuple_coor = parsing_str_to_int(coor_str)
    if not tuple_coor:
        # Continues without any action
        pass

    print("\nUnpacking demonstration:")
    pos = (3, 4, 0)
    x, y, z = pos
    print(f"Player at: x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    coordinates_test()
