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

        for char in argv:
            if char == ":":
                found_colon = True
                continue  # Skips the colon (":"") found char

            # As long as the colon is not found, keep the
            # chars found in the 'name' variable
            if not found_colon:
                name += char
            # If the colon is found, pass it (continue) and keep the
            # next chars in the 'value' variable
            else:
                value += char

        # Once they are filled, put them in the dictionary if data was correct
        if name != "" and value != "":
            try:
                inventory.update({name: int(value)})
            except ValueError as e:
                print(f"Error: {e}")
                pass  # Skips it if it was incorrect after printing the warning


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

        # Get if unit/units:
        if value == 1:
            unit_str = "unit"
        else:
            unit_str = "units"

        # Print all together
        print(f"{name}: {value} {unit_str} ({percentage:.1f}%)")


def highest_value(inventory: dict) -> None:
    """
    Find and print the most abundant item in the inventory.
    """
    # Initialized values
    h_name = ""
    h_value = -1
    # Compares each element of the dict to find the highest
    for name, value in inventory.items():
        if value > h_value:
            h_value = value
            h_name = name
    # Assigns unit/units
    if h_value == 1:
        units_str = "unit"
    else:
        units_str = "units"
    print(f"Most abundant: {h_name} ({h_value} {units_str})")


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
        if l_value == -1 or value < l_value:
            l_value = value
            l_name = name
    # Assigns unit/units
    if l_value == 1:
        units_str = "unit"
    else:
        units_str = "units"
    print(f"Least abundant: {l_name} ({l_value} {units_str})")


def moderate_inventory(inventory: dict):
    """
    Identify and display items with a quantity of 5 or more.
    """
    mod = dict()
    for name, value in inventory.items():
        # If an item's value is more than or 5, it adds to the mod
        if value >= 5:
            mod.update({name: value})
    if not mod:
        print("There are no moderate elements")
    else:
        print(f"Moderate: {mod}")


def scarce_inventory(inventory: dict):
    """
    Identify and display items with a quantity of less than 5.
    """
    sca = dict()
    for name, value in inventory.items():
        # If an item's value is more than or 5, it adds to the mod
        if value < 5:
            sca.update({name: value})
    if not sca:
        print("There are no scarce elements")
    else:
        print(f"Scarce: {sca}")


def ft_inventory_system() -> None:
    """
    Execute the main inventory management and reporting system.
    """
    # Control no input in command line
    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py item:qty ...")
        return

    inventory = dict()
    # Parsing each element and setting it in the dict()
    parsing_command_argument_into_dict(inventory)
    if not inventory:
        return
    else:
        print(f"{inventory}")

    print("=== Inventory System Analysis ===")
    # Get the amount of values in the dict going through the list of values
    # in the dict ([dict].values() -> list of values inside)
    total_values = 0
    for i in inventory.values():
        total_values += i
    print(f"Total items in inventory: {total_values}")

    # Get the number of keys(name: value) that the dict contains
    print(f"Unique item types: {len(inventory)}\n")

    # Get the list of items, their amounts, units and percentage
    print("=== Current Inventory ===")
    current_inventory(inventory, total_values)

    # Get the item with the highest and lowest value
    print("\n=== Inventory Statistics ===")
    highest_value(inventory)
    lowest_value(inventory)

    # Get the items that has most/scarce (few) units
    print("\n=== Item Categories ===")
    moderate_inventory(inventory)
    scarce_inventory(inventory)

    print("\n=== Management Suggestions ===")
    # Signals the items that have a value of 1 or less
    restock = ""
    for name, value in inventory.items():
        if value <= 1:
            # Creates a string that accumulates the names of the items, adding
            # commas, if there are more than 1 item already in the string
            if (len(restock) > 0):
                restock += ", "
            restock += name
    print(f"Restock needed: {restock}\n")

    print("=== Dictionary Properties Demo ===")
    # Get the keys names in a single string
    keys = ""
    for i in inventory.keys():
        # if there are elements already, separate them with commas
        if len(keys) > 0:
            keys += ", "
        keys += i
    print(f"Dictionary keys: {keys}")

    # Same logic but with values
    # Get the values in a single string
    values = ""
    for i in inventory.values():
        # if there are elements already, separate them with commas
        if len(values) > 0:
            values += ", "
        # Converts the int() to a str() by using the f"{i}"
        values += f"{i}"
    print(f"Dictionary values: {values}")

    # Checks if an specific item exists
    item = "sword"
    # Gives you the value of the searched item
    qty_item = inventory.get(item)
    if qty_item:
        bool_item = True
    else:
        bool_item = False
    print(f"Sample lookup - '{item}' in inventory: {bool_item}")


if __name__ == "__main__":
    ft_inventory_system()
