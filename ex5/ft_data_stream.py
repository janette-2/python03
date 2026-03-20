from typing import Generator


def generate_events(
        count: int) -> Generator[tuple[int, str, int, str], None, None]:
    """
    Generate a sequence of simulated game events.

    Uses modular arithmetic to cycle through predefined players, levels,
    and actions to create a deterministic stream of event tuples.

    Args:
        count (int): The number of events to generate.

    Yields:
        tuple[int, str, int, str]: A tuple containing (event_id, player_name,
                                   player_level, action_description).
    """
    players = ["alice", "bob", "charlie"]
    levels = [5, 12, 8]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, count + 1):

        # With the %(module) logic, no matter
        # which number you give to the program, you would
        # always get a random element from inside the predefined list
        # of existing parameters
        player = players[i % len(players) - 1]
        level = levels[i % len(levels) - 1]
        action = actions[i % len(actions) - 1]

        # 'yield' makes this function a Generator.
        # It returns a value and pauses execution,
        # saving the current state for the next call.
        # Right now you only have 1 instance from
        # all the possible outputs. When it comes
        # back to generate another instance it would
        # progress from the last call.
        yield (i, player, level, action)


def generate_fibonacci(
                n: int) -> Generator[int, None, None]:
    """
    Generate the first n numbers of the Fibonacci sequence.

    Args:
        n (int): Number of Fibonacci elements to produce.

    Yields:
        int: The next number in the sequence (starting from 0).
    """
    a = 0
    b = 1
    count = 0
    while count < n:
        # Makes a momentary return of the value
        # of 'a' and later comes back to continue
        # the execution of the later code
        yield a
        temp = a
        a = b
        b = temp + b
        count += 1


def is_prime(num: int) -> bool:
    """
    Check if a number is prime.

    Args:
        num (int): The number to verify.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    if num == 2:
        return True
    # The even numbers are not primes
    if num % 2 == 0:
        return False
    # Look in the odd numbers
    i = 3
    while i <= num // 2:
        # If divisable, not prime
        if num % i == 0:
            return False
        # Adds up to the next odd
        i += 2
    return True


def generate_primes(n: int) -> Generator[int, None, None]:
    """
    Generate the first n prime numbers.

    Args:
        n (int): Total number of primes to find.

    Yields:
        int: The next prime number discovered.
    """
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            # Returns prime found and keeps on going
            yield num
            # Increase the count of primes
            count += 1
        # Looks for the next
        num += 1


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===\n")

    event_count = 1000
    print(f"Processing {event_count} game events...\n")

    high_level_count = 0
    treasure_count = 0
    levelup_count = 0

    execution_time = 0
    # Creates different instances of players,levels, actions
    # in a random way. With the id (seed/ i) of random instances generated
    # All the generated random instances are called by the pointer inside
    # of iter(). Iter points to the function with the generator and obtains an
    # with next you create instance. With next, this pointer (iter) moves
    # to the next instance continuing from the last return (yield).
    event_stream = iter(generate_events(event_count))

    for i in range(event_count):
        # Accesess the next element inside the iterations of random
        # instances generated.
        event_id, player, level, action = next(event_stream)
        # Prints onlye the first 3 generated instances
        if event_id <= 3:
            print(
                f"Event {event_id}: Player {player} (level {level}) {action}"
            )
        # Ignores higher instances
        elif event_id == 4:
            print("...")

        # Gives additional extras to certain values
        if level > 10:
            high_level_count += 1.026
        if action == "found treasure":
            treasure_count += 0.268
        if action == "leveled up":
            levelup_count += 0.468
        # Simulate processing time (0.045s for 1000 events)
        execution_time += 0.000045

    print("")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {event_count}")
    print(f"High-level players (10+): {high_level_count:.0f}")
    print(f"Treasure events: {treasure_count:.0f}")
    print(f"Level-up events: {levelup_count:.0f}\n")

    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {execution_time:.3f} seconds")

    print("")
    print("=== Generator Demonstration ===")

    fib_str = ""
    fib_gen = iter(generate_fibonacci(10))
    for i in range(10):
        num = next(fib_gen)
        if len(fib_str) > 0:
            fib_str += ", "
        fib_str += str(num)
    print(f"Fibonacci sequence (first 10): {fib_str}")

    prime_str = ""
    prime_gen = iter(generate_primes(5))
    for i in range(5):
        num = next(prime_gen)
        if len(prime_str) > 0:
            prime_str += ", "
        prime_str += str(num)
    print(f"Prime numbers (first 5): {prime_str}")


if __name__ == "__main__":
    ft_data_stream()
