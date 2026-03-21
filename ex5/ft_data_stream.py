import typing
import random


def gen_events(
        count: int) -> typing.Generator[tuple[str, str], None, None]:
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
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release"]

    for i in range(1, count + 1):

        # With the %(module) logic, no matter
        # which number you give to the program, you would
        # always get a random element from inside the predefined list
        # of existing parameters
        player = players[i % len(players) - 1]
        action = actions[i % len(actions) - 1]

        # 'yield' makes this function a Generator.
        # It returns a value and pauses execution,
        # saving the current state for the next call.
        # Right now you only have 1 instance from
        # all the possible outputs. When it comes
        # back to generate another instance it would
        # progress from the last call.
        yield (player, action)


def consume_events(list_tuples: list[tuple]):
    """ Deletes the list by choosing random objects
    and returning each instance and current state of
    the  list while deleting it"""

    while len(list_tuples) > 0:
        tuple_rm = random.choice(list_tuples)
        new_list = []
        for i in list_tuples:
            if i != tuple_rm:
                new_list += [i]
        list_tuples = new_list
        # Prints all the tuples randomly picked,
        # and the current state of the list after deleting it
        yield (f"Got event from list: {tuple_rm}\n"
               f"Remains in list: {list_tuples}")


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")

    event_count = 1000

    # Creates different instances of players,levels, actions
    # in a random way. With the id (seed/ i) of random instances generated
    # All the generated random instances are called by the pointer inside
    # of iter(). Iter points to the function with the generator and obtains an
    # with next you create instance. With next, this pointer (iter) moves
    # to the next instance continuing from the last return (yield).
    event_stream = iter(gen_events(event_count))

    for i in range(event_count):
        # Accesess the next element inside the iterations of random
        # instances generated.
        player, action = next(event_stream)
        print(f"Event {i}: Player {player} did action {action}")

    # List of tuples generated with gen_event()
    list_tuples = []
    # Pointer to the generator that will give 10 random combinations
    event_tuples = iter(gen_events(10))
    # Filling the list by calling the next combination generatesd each time
    for i in range(10):
        list_tuples += [tuple(next(event_tuples))]
    # Final list
    print(f"Built list of 10 events: {list_tuples}")
    # To see all the steps of the yield (generator) we need to
    # print all of the yields triggered in a for .. in structure
    for list in consume_events(list_tuples):
        print(list)


if __name__ == "__main__":
    ft_data_stream()
