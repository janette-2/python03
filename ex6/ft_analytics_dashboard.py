def ft_analytics_dashboard() -> None:
    """
    Analyzes game data using various Python comprehensions.
    Displays player scores, categories, and achievement statistics.
    """
    print("=== Game Analytics Dashboard ===")

    # Sets with the data of the players
    players = [
        {
            "name": "alice", "score": 2300,
            "achievements": [
                "first_kill", "level_10", "boss_slayer",
            ],
            "active": True, "region": "north"
        },
        {
            "name": "bob", "score": 1800,
            "achievements": ["first_kill", "level_10", "boss_slayer"],
            "active": True, "region": "east"
        },
        {
            "name": "charlie", "score": 2150,
            "achievements": [
                "first_kill", "level_10", "boss_slayer"
            ],
            "active": True, "region": "central"
        },
        {
            "name": "diana", "score": 2000,
            "achievements": ["level_10", "boss_slayer", "first_kill"],
            "active": False, "region": "north"
        }
    ]

    print("=== List Comprehension Examples ===")

    # Gets a list of names from the players[] getting the ones that
    # have a score higher than 2000
    high_scorers = [person["name"] for person in players if
                    person["score"] >= 2000]
    print(f"High scorers (>=2000): {high_scorers}")

    # Gets a list of scores from the players[] doubled
    scores_doubled = [person["score"] * 2 for person in players]
    print(f"Scores doubled: {scores_doubled}")

    # Gets a list of the active players from players[]
    active_players = [person["name"] for person in players if person["active"]]
    print(f"Active players: {active_players}")

    print()

    print("=== Dict Comprehension Examples ===")
    # Get a dictionary of the active players with their scores
    players_scores = {person["name"]: person["score"] for person in players
                      if person["active"]}
    print(f"Player scores: {players_scores}")

    # Makes a list with the scores that fit the ranges and get theit len()
    # to assign the value to the category
    score_categories = {"high": len([person["score"] for person in players
                                     if person["score"] >= 2000]),
                        "medium": len([person["score"] for person in players
                                      if 1800 < person["score"] < 2300]),
                        "low": len([person["score"] for person in players
                                    if person["score"] <= 1800])}

    print(f"Score categories: {score_categories}")

    # Get the list of achievemets of each player and gets the len()
    a_counts = {person["name"]: len(person["achievements"]) for person
                in players if person["active"]}
    print(f"Achievement counts: {a_counts}")
    print()

    print("=== Set Comprehension Examples ===")
    unique_players = {person["name"] for person in players}
    print(f"Unique players: {unique_players}")

    # A loop inside of a loop. First gets the person, inside the person reads
    # the achievements and recovers all the achievements found,
    # and because its a set, it won't have duplicates
    ac = {ach for person in players for ach in person["achievements"]}
    print(f"Unique achievements: {ac}")

    active_regions = {person["region"] for person in players
                      if person["active"]}
    print(f"Active regions: {active_regions}")
    print()

    print("=== Combined Analysis ===")
    print(f"Total players: {len(players)}")

    print(f"Total unique achievements: {len([ach for person in players for ach
                                             in person["achievements"]])}")

    total_scores = sum([person["score"] for person in players])
    avg_score = total_scores / len(players) if players else 0
    print(f"Average score: {avg_score}")

    max_score = max([person["score"] for person in players])
    top_performer = [person for person in players
                     if person["score"] == max_score][0]
    # top_performer is a list, even though it has only an element,
    # you need to specify that you only want to access that element:
    # top_performer[0]

    n = top_performer['name']
    s = top_performer['score']
    a = len(top_performer['achievements'])
    print(f"Top performer: {n} ({s} points, {a} achievements)")


if __name__ == "__main__":
    ft_analytics_dashboard()
    try:
        ft_analytics_dashboard()
    except (ValueError, ZeroDivisionError, IndexError) as e:
        print(f"Error: {e}")
