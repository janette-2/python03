import sys


def receive_parameters() -> None:
    if (len(sys.argv) < 2):
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {len(sys.argv)}")
        return
    else:
        total_arguments = len(sys.argv) - 1

        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {total_arguments}")

        for arg in range(1, len(sys.argv)):
            c_str: str = sys.argv[arg]
            c_int: int = 0
            try:
                c_int = int(c_str)
            except ValueError as e:
                print(f"Invalid input: {str(e)}")

            print(f"Argument {arg}: {c_int}")

        print(f"Total arguments: {len(sys.argv)}")
        return


if __name__ == "__main__":
    print("=== Command Quest ===")
    receive_parameters()
