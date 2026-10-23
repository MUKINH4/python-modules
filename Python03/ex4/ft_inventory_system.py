from sys import argv


def parse_inventory(arguments: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for parameter in arguments:
        parts = parameter.split(":")
        if len(parts) != 2 or not parts[0]:
            print(f"Error - invalid parameter '{parameter}'")
            continue

        item, quantity_text = parts
        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            quantity = int(quantity_text)
        except ValueError as error:
            print(f"Quantity error for '{item}': {error}")
            continue

        inventory[item] = quantity

    return inventory


def print_inventory_analysis(inventory: dict[str, int]) -> None:
    items = list(inventory.keys())
    quantities = list(inventory.values())
    total_quantity = sum(quantities)

    print("Got inventory:", inventory)
    print("Item list:", items)
    print(f"Total quantity of the {len(items)} items: {total_quantity}")

    if not inventory or total_quantity == 0:
        return

    for item, quantity in inventory.items():
        percentage = round(quantity / total_quantity * 100, 1)
        print(f"Item {item} represents {percentage}%")

    most_abundant = items[0]
    least_abundant = items[0]
    for item in items[1:]:
        if inventory[item] > inventory[most_abundant]:
            most_abundant = item
        if inventory[item] < inventory[least_abundant]:
            least_abundant = item

    print(
        f"Item most abundant: {most_abundant} "
        f"with quantity {inventory[most_abundant]}"
    )
    print(
        f"Item least abundant: {least_abundant} "
        f"with quantity {inventory[least_abundant]}"
    )


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = parse_inventory(argv[1:])
    print_inventory_analysis(inventory)
    inventory.update({"magic_item": 1})
    print("Updated inventory:", inventory)


if __name__ == "__main__":
    main()
