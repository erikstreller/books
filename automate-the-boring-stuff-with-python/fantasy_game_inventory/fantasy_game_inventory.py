# fantasy_game_inventory.py

def display_inventory(inventory: dict) -> None:
    print("Inventory:")
    print("----------")
    itemTotal = 0

    for item, quantity in inventory.items():
        print(f"{str(quantity)} {item}")
        itemTotal += quantity

    print(f"\nTotal number if items: {str(itemTotal)}\n")


def add_to_inventory(inventory: dict, addedItems: list) -> dict:
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1

    return inventory


if __name__ == "__main__":

    stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
    dragonLoot = ["gold coin", "dagger", "gold coin", "bow", "ruby"]

    display_inventory(stuff)
    newStuff = add_to_inventory(stuff, dragonLoot)
    display_inventory(newStuff)
