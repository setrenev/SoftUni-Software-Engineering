products = {}

command = input()

while not command == "buy":
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products:
        products.update({name: [price, quantity]})
    else:
        products[name][0] = price
        products[name][1] += quantity

    command = input()

for name, stock in products.items():
    amount = products.get(name)[0] * products.get(name)[1]
    print(f"{name} -> {amount:.2f}")
