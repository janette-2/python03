import sys


def receive_parameters() -> None:
    """
    Process and display command-line arguments.

    This function identifies the program name and iterates through
    all provided arguments, printing their index and value.
    """
    if (len(sys.argv) < 2):
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {len(sys.argv)}")
        return
    else:
        total_arguments = 0
        for arg in sys.argv:
            total_arguments += 1
        total_arguments -= 1  # Minus the program name
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {total_arguments}")
        for arg in range(1, len(sys.argv)):  # arg serves as the counter 'i'
            print(f"Argument {arg}: {sys.argv[arg]}")
        print(f"Total arguments: {len(sys.argv)}")
        return


if __name__ == "__main__":
    print("=== Command Quest ===")
    receive_parameters()
