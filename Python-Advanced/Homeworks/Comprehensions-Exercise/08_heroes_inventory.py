inventory = {}

[inventory.update({el: {"get_items": [], "Items": 0, "Cost": 0}}) for el in input().split(", ")]

while True:
    line = input()
    if line == "End":
        break

    name, item, cost = line.split("-")
    if item not in inventory[name]["get_items"]:
        inventory[name]["get_items"].append(item)
        inventory[name]["Cost"] += int(cost)
        inventory[name]["Items"] += 1

for name, data in inventory.items():
    data.pop("get_items")
    print(f"{name} ->", end=" ")
    print(*[f"{key}: {value}"for key, value in data.items()], sep=", ")
