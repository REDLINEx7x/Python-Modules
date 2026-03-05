import sys


def sorting(items_list: list) -> None:
    i = 0
    while i < len(items_list):
        j = i + 1
        while j < len(items_list):
            if items_list[j][1] > items_list[i][1]:
                temp = items_list[i]
                items_list[i] = items_list[j]
                items_list[j] = temp
            j += 1
        i += 1


def find_max(numbers) -> int:
    x = 0
    for i in numbers:
        if i > x:
            x = i
    return x


def find_min(numbers) -> int:
    x = find_max(numbers)
    for i in numbers:
        if i < x:
            x = i
    return x


if __name__ == "__main__":
    first_inventory = {}
    values_count = 0
    is_valid = True
    usage_message = (
        "\nUsage: python3 ft_inventory_system.py item:count [item:count ...]\n"
        "Example: python3 ft_inventory_system.py sword:1 potion:5\n"
    )

    # 2. Check if arguments exist
    if len(sys.argv) <= 1:
        is_valid = False
    else:
        # 3. Parse and Validate
        for i in sys.argv[1:]:
            if ":" not in i:
                is_valid = False
                break

            item = i.split(":")
            try:
                key = item[0]
                value = int(item[1])
                # Ensure key isn't empty and value is positive
                if not key or value < 0:
                    is_valid = False
                    break
                first_inventory[key] = value
                values_count += value
            except (ValueError, IndexError):
                is_valid = False
                break

    # 4. Final Decision: Run Analysis OR Show Usage
    if is_valid and first_inventory:
        print("=== Inventory System Analysis ===")
        print(f"Total items in inventory: {values_count}")
        print(f"Unique item types: {len(first_inventory)}\n")

        print("=== Current Inventory ===")

        items_list = list(first_inventory.items())
        sorting(items_list)
        for item in items_list:
            name = item[0]
            val = item[1]
            percent = (val / values_count) * 100

            if val > 1:
                print(f"{name}: {val} units ({percent:.1f}%)")
            else:
                print(f"{name}: {val} unit ({percent:.1f}%)")
        print()

        inventory = dict(items_list)
        maxi = find_max(inventory.values())
        mini = find_min(inventory.values())
        print("=== Inventory Statistics ===")
        for name in inventory:
            if inventory.get(name) == maxi:
                print(f"Most abundant: {name} ({maxi} units)")
            elif inventory.get(name) == mini:
                print(f"Least abundant: {name} ({mini} unit)")
                break
        print()
        print("=== Item Categories ===")
        categories = {"Moderate": {}, "Scarce": {}}
        i = 0
        while i < len(items_list):
            k = items_list[i][0]
            v = items_list[i][1]
            if v >= 4:
                categories["Moderate"].update({k: v})
            else:
                categories["Scarce"].update({k: v})
            i += 1

        for category, item in categories.items():
            print(f"{category}: {item}")

        print()
        print("=== Management Suggestions ===")

        out_list = []
        scarce_items = categories.get("Scarce")

        for name, val in scarce_items.items():
            if val == 1:
                out_list.append(name)
        restock = ", ".join(out_list)
        print(f"Restock needed: {restock}")
        print()
        print("=== Dictionary Properties Demo ===")
        keys = ", ".join(first_inventory.keys())
        print(f"Dictionary keys: {keys}")

        inventory_values = list(first_inventory.values())
        string_values = []

        i = 0
        while i < len(inventory_values):
            string_values.append(str(inventory_values[i]))
            i += 1
        values_output = ", ".join(string_values)
        print(f"Dictionary values: {values_output}")
        lookup_result = 'sword' in first_inventory
        print(f"Sample lookup - 'sword' in inventory: {lookup_result}")
    else:
        print(usage_message)
