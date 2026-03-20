import sys


def scores_analysis() -> None:
    """
    Parse command-line arguments as integers and perform statistical analysis.

    The function calculates the total, average, maximum, minimum, and range
    of the provided scores. It handles invalid non-integer inputs gracefully.
    """
    scores = []
    if (len(sys.argv) < 2):
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return
    i = 0
    for i in range(1, len(sys.argv)):
        try:
            scores += [int(sys.argv[i])]
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
    if not scores:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores)/len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    scores_analysis()
