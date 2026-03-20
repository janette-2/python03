def ft_achievement_tracker() -> None:
    """
    Analyze and display player achievement data using set operations.

    This function demonstrates union, intersection, and difference
    to track unique, common, and rare achievements among players.
    """
    print("=== Achievement Tracker System ===\n")

    # Declaring sets (list of unique data, without duplicates) == set(list[])
    # or set = {el1, el2, ...}
    alice_set = set(["first_kill", "level_10", "treasure_hunter",
                     "speed_demon"])
    bob_set = set(["first_kill", "level_10", "boss_slayer", "collector"])
    charlie_set = set(["level_10", "treasure_hunter", "boss_slayer",
                      "speed_demon", "perfectionist"])

    # Printing sets (sets don't print the elements in order, it has no indexes)
    # sets work with hash (convertion of a text into an int and recognition of each
    # element through their int representation)
    print(f"Player alice achievements:{alice_set}")
    print(f"Player bob achievements:{bob_set}")
    print(f"Player charlie achievements:{charlie_set}\n")

    print("=== Achievement Analytics ===")
    # Union
    all_achieve = alice_set.union(bob_set).union(charlie_set)
    print(f"All unique achievements: {all_achieve}")
    print(f"Total unique achievements: {len(all_achieve)}\n")

    # Intersection
    common = alice_set.intersection(bob_set).intersection(charlie_set)
    print(f"Common to all players: {common}")

    # Difference
    # Unique achievements that only has each player
    alice_only = alice_set.difference(bob_set).difference(charlie_set)
    bob_only = bob_set.difference(alice_set).difference(charlie_set)
    charlie_only = charlie_set.difference(alice_set).difference(bob_set)
    # Union of all the achievements that only a player posses
    uniques = alice_only.union(bob_only).union(charlie_only)
    print(f"Rare achievements (1 player): {uniques}\n")

    # Alice vs Bob
    #  Compare particular sets intersections
    al_and_bob = alice_set.intersection(bob_set)
    print(f"Alice vs Bob common: {al_and_bob}")
    # Alice unique achivements
    al_only = alice_set.difference(bob_set)
    print(f"Alice unique: {al_only}")
    # Bob unique achievements
    bob_only = bob_set.difference(alice_set)
    print(f"Bob unique: {bob_only}")


if __name__ == "__main__":
    ft_achievement_tracker()
