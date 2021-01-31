item_list = input().split("|")
budget = float(input())

profit = 0
sold_item_price = []

for item in item_list:
    item_name, item_price = item.split("->")
    item_price = float(item_price)
    current_profit = 0

    if item_name == "Clothes" and item_price > 50:
        continue
    elif item_name == "Shoes" and item_price > 35:
        continue
    elif item_name == "Accessories" and item_price > 20.5:
        continue

    if item_price > budget:
        continue

    budget -= item_price
    current_profit = item_price * 0.4
    profit += current_profit
    sold_item_price.append(item_price + current_profit)

budget += sum(sold_item_price)

for sell_item in sold_item_price:
    print(f"{sell_item:.2f}", end=" ")

print()
print(f"Profit: {profit:.2f}")

if budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
