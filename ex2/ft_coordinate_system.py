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


def parsing_input() -> tuple[int, int, int]:
    """
    Prompt the user for 3D coordinates and parse the input string.

    Uses recursion to re-prompt the user in case of invalid syntax
    or non-numeric values until a valid tuple is provided.

    :return: A tuple containing three integers (x, y, z).
    """
    pos1 = input("Enter new coordinates as floats in format 'x,y,z': ")
    separated = pos1.split(",")
    count = 0
    for i in separated:
        count += 1
    if count < 3:
        print("Invalid syntax")
        # Stops the execution by giving the result of the new call
        # avoiding dragging trash in the new data and continuing old code
        return parsing_input()
    float_list = []
    i = 0
    try:
        for i in separated:
            float_list += [float(i)]
    except ValueError as e:
        print(f"Error on parameter '{i}': {e}")
        return parsing_input()
    return tuple(float_list)


def coordinates_test() -> None:
    """
    Run a demonstration of coordinate parsing and distance calculation.

    It asks for two sets of coordinates, displays their components,
    and calculates distances to the origin and between each other.
    """
    print("=== Game Coordinate System ===\n")

    pos1 = parsing_input()
    print(f"Got a first tuple: {pos1}")
    x1, y1, z1 = pos1
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    dis1 = distance((0, 0, 0), pos1)
    print(f"Distance to center: {dis1:.4f}\n")

    print("Got a second set of coordinates")
    pos2 = parsing_input()
    dis2 = distance(pos1, pos2)
    print(f"Distance between the 2 sets of coordinates: {dis2:.4f}\n")


if __name__ == "__main__":
    coordinates_test()
