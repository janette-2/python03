import random


def ft_analytics_dashboard() -> None:
    """
    Analyzes game data using various Python comprehensions.
    Displays player scores, categories, and achievement statistics.
    """

    names_list = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam"
    ]

    print(f"Initial list of players: {names_list}")
    # List comprehensions :
    cap_names = [(i[0].upper() + i[1:]) for i in names_list]
    print(f"New list with all names capitalized: {cap_names}")

    orig_cap = [i for i in names_list if i[0] == i[0].upper()]
    print(f"New list of capitalized names only: {orig_cap}\n")

    # Dict comprehensions:
    # Create an action with comprehension, using the method to assing
    # keys to a dictionary (name : value) for i in xxx
    dict_cap = {name: random.randint(0, 1000) for name in cap_names}
    print(f"Score dict: {dict_cap}")

    # Scores average
    scores = 0
    keys = 0
    for key in dict_cap:
        # Getting the value of each key
        scores += dict_cap[key]
        keys += 1
    scores_avg = scores/keys
    print(f"Score average is {scores_avg:.2f}")

    high_scores = {name: dict_cap[name] for name in dict_cap
                   if dict_cap[name] > scores_avg}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    ft_analytics_dashboard()
    try:
        ft_analytics_dashboard()
    except (ValueError, ZeroDivisionError, IndexError) as e:
        print(f"Error: {e}")
