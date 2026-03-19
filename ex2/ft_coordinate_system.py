import math


def distance(tuple1: tuple[int, int, int], tuple2: tuple[int, int, int]) -> float:
    """Tuples are a type of data that doesn't let you alter its 
    content after its creation"""
    x1, y1, z1 = tuple1  # Separated by the 'unpacking' technique
    x2, y2, z2 = tuple2
    distance = math.sqrt(((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))
    return distance


def parsing_str_to_int(coor_str: list[str]) -> list[int] | None:
    coor_ints = []
    try:
        for i in coor_str:
            coor_ints += [int(i)]
    except ValueError as e:
        print(f"Error parsing coodinates: {e}")
        return
    return coor_ints


def coordinates_test() -> None:
    print("=== Game Coordinate System ===\n")

    pos = (10, 20, 5)  # structure to declare a tuple: var = (x, y, z)
    pos0 = (0, 0, 0)
    dis = distance(pos0, pos)
    print(f"Position created: {pos}")
    # The dis:.2f allows you to choose the decimals to show (2 in here)
    print(f"Distance between {pos0} and {pos}: {dis:.2f}\n")

    coor_str = "3,4,0"
    print(f"Parsing coodinates: {coor_str}")
    coor_list = coor_str.split(",")  # split needs the separator char and returns the list separated
    coor_int = parsing_str_to_int(coor_list)
    if not coor_int:
        raise ValueError:
    print(f"Parsed position: {tuple(coor_int)}")

if __name__ == "__main__":
    coordinates_test()
