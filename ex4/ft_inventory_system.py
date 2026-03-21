import sys


def parsing_command_argument_into_dict(inventory: dict) -> None:
    """
    Parse command-line arguments in 'name:value' format into a dictionary.

    Iterates through sys.argv, splits strings by the colon character,
    and updates the inventory with integer values.
    """
    # Goes through all the arguments passed starting from sys.argv[1]
    #  and on (sys.argv[1:])
    for argv in sys.argv[1:]:
        name = ""
        value = ""
        found_colon = False
        i = 0
        for char in argv:
            i += 1
            if char == ":":
                found_colon = True
                continue  # Skips the colon (":"") found char

            # As long as the colon is not found, keep the
            # chars found in the 'name' variable
            if not found_colon:
                name += char
                # If it doesn't have a item:value structure..
                if i == len(argv):
                    print(f"Error - invalid parameter '{argv}'")
                    # Empty the found 'name' to avoid updating
                    # it in the dictionary
                    name = ""
            # If the colon is found, pass it (continue) and keep the
            # next chars in the 'value' variable
            else:
                value += char

        # Once they are filled, put them in the dictionary if data was correct
        if name != "" and value != "":
            if inventory.get(name):
                print(f"Redundant item '{name}' - discarding")
                # Skips it if it was redundant after printing the warning
                pass
            else:
                try:
                    inventory.update({name: int(value)})
                except ValueError as e:
                    print(f"Quantity error for '{name}': {e}")
                    # Skips it if it was incorrect after printing the warning
                    pass


def current_inventory(inventory: dict, total_values: int) -> None:
    """ Get each element value and name, differentiate if
    they are getting a unit/units (value==1?) and get their
    percentage in correlation to the total of values.
    """
    for name, value in inventory.items():
        # Items get the pair of name and value

        # Get the percentage
        if total_values == 0:
            percentage = 0
        else:
            percentage = (value * 100) / total_values

        # Print all together
        print(f"Item {name} represents {percentage:.1f}%")


def highest_value(inventory: dict) -> None:
    """
    Find and print the most abundant item in the inventory.
    """
    # Initialized values
    h_name = ""
    h_value = -1
    # Compares each element of the dict to find the highest
    for name, value in inventory.items():
        # If it founds one with the same value (=), it doesn't update
        # getting always the first one that was found in sys.argv[]
        if value > h_value:
            h_value = value
            h_name = name
    print(f"Item most abundant: {h_name} with quantity {h_value}")


def lowest_value(inventory: dict) -> None:
    """
    Find and print the least abundant item in the inventory.
    """
    # Initialized values
    l_name = ""
    l_value = -1
    # Compares each element of the dict to find the lowest,
    # gets the first element always.
    for name, value in inventory.items():
        # If it founds one with the same value(=), it doesn't update
        # getting always the first one that was found in sys.argv[]
        if l_value == -1 or value < l_value:
            l_value = value
            l_name = name
    print(f"Item least abundant: {l_name} with quantity {l_value}")


def new_item(inventory: dict, name: str, value: int) -> None:
    """
    Updates a specific dictionary with the passed name and value
    """
    inventory.update({name: value})


def ft_inventory_system() -> None:
    """
    Execute the main inventory management and reporting system.
    """
    # Control no input in command line
    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py item:qty ...")
        return
    print("=== Inventory System Analysis ===")
    inventory = dict()
    # Parsing each element and setting it in the dict(), printing it if found
    parsing_command_argument_into_dict(inventory)
    if not inventory:
        return
    else:
        print(f"Got inventory: {inventory}")

    # Get the keys of the items found in the inventory
    items = []
    for i in inventory.keys():
        items += [i]
    print(f"Item list: {items}")

    # Get the total of all the items values together
    total_values = 0
    for i in inventory.values():
        total_values += i
    print(f"Total quantity of the {len(inventory.keys())} "
          f"items: {total_values}")

    # Get the list of items and their percentage
    current_inventory(inventory, total_values)

    # Get the item most and least abundant, by the highest/lowest value
    highest_value(inventory)
    lowest_value(inventory)

    # Add a new key
    new_item(inventory, "magic_item", 1)
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    ft_inventory_system()
