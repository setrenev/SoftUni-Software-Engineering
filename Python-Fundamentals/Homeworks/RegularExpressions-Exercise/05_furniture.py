import re

furniture = {"name": [], "amount": 0}

pattern = r"^>>(?P<name>[a-zA-Z]+)<<(?P<price>\d+[.]?\d+)!(?P<qty>\d+)$"

command = input()

while not command == "Purchase":
    purchase = re.finditer(pattern, command)
    purchase = [el.groupdict() for el in purchase]

    if purchase:
        name_of_item = purchase[0]["name"]
        amount_of_item = float(purchase[0]["price"]) * int(purchase[0]["qty"])
        furniture["name"].append(name_of_item)
        furniture["amount"] += amount_of_item

    command = input()

total_money = furniture["amount"]

print("Bought furniture:")
[print(item) for item in furniture["name"]]
print(f"Total money spend: {total_money:.2f}")