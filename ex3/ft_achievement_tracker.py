def ft_achievement_tracker() -> None:
    """
    Analyze and display player achievement data using set operations.

    This function demonstrates union, intersection, and difference
    to track unique, common, and rare achievements among players.
    """
    print("=== Achievement Tracker System ===\n")

    # Declaring sets (list of unique data, without duplicates) == set(list[])
    # or set = {el1, el2, ...}
    alice_set = set(["Crafting Genius", "World Savior", "Master Explorer",
                     "Collector Supreme", "Untouchable", "Boss Slayer"])
    charlie_set = set(["Strategist", "Speed Runner", "Survivor",
                       "Master Explorer", "Treasure Hunter", "First Steps",
                       "Collector Supreme", "Untouchable", "Sharp Mind"])
    bob_set = set(["Crafting Genius", "Strategist", "World Savior",
                   "Master Explorer", "Unstoppable", "Collector Supreme",
                   "Untouchable"])
    dylan_set = set(["Strategist", "Speed Runner", "Unstoppable",
                     "Untouchable", "Boss Slayer"])

    # Printing sets (sets don't print the elements in order, it has no indexes)
    # sets work with hash (convertion of a text into an int and recognition of
    # each element through their int representation)
    print(f"Player Alice:{alice_set}")
    print(f"Player Bob:{bob_set}")
    print(f"Player Charlie:{charlie_set}")
    print(f"Player Dylan :{dylan_set}\n")

    # Union (aggregates everything)
    all_achieve = alice_set.union(bob_set).union(charlie_set).union(dylan_set)
    print(f"All unique achievements: {all_achieve}\n")

    # Intersection (common to everyone)
    common = alice_set.intersection(bob_set).intersection(
        charlie_set).intersection(dylan_set)
    print(f"Common to all players: {common}\n")

    # Difference
    # Unique achievements that only has each player
    alice_only = alice_set.difference(bob_set).difference(
        charlie_set).difference(dylan_set)
    print(f"Only Alice has: {alice_only}")
    bob_only = bob_set.difference(alice_set).difference(
        charlie_set).difference(dylan_set)
    print(f"Only Bob has: {bob_only}")
    charlie_only = charlie_set.difference(alice_set).difference(
        bob_set).difference(dylan_set)
    print(f"Only Charlie has: {charlie_only}")
    dylan_only = dylan_set.difference(alice_set).difference(
        bob_set).difference(charlie_set)
    print(f"Only Dylan has: {dylan_only}\n")

    #  Compare particular sets intersections
    hidden_set = {"Hidden Path Finder"}

    alice_missing = bob_set.difference(alice_set).union(charlie_set.difference(
        alice_set)).union(dylan_set.difference(alice_set)).union(
            hidden_set.difference(alice_set))
    print(f"Alice is missing: {alice_missing}")

    bob_missing = alice_set.difference(bob_set).union(charlie_set.difference(
        bob_set)).union(dylan_set.difference(bob_set)).union(
            hidden_set.difference(bob_set))
    print(f"Bob is missing: {bob_missing}")

    charlie_missing = alice_set.difference(charlie_set).union(
                    bob_set.difference(charlie_set)).union(
                    dylan_set.difference(charlie_set)).union(
                    hidden_set.difference(charlie_set))
    print(f"Charlie is missing: {charlie_missing}")

    dylan_missing = alice_set.difference(dylan_set).union(
                    bob_set.difference(dylan_set)).union(
                    charlie_set.difference(dylan_set)).union(
                    hidden_set.difference(dylan_set))
    print(f"Charlie is missing: {dylan_missing}")


if __name__ == "__main__":
    ft_achievement_tracker()
