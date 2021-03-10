command = input()
prices = []

while not (command == "special" or command == "regular"):
    current_price = float(command)
    if current_price > 0:
        prices.append(current_price)
    else:
        print("Invalid price!")

    command = input()

total_price = sum(prices)
taxes = total_price * 0.2

if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    total_price += taxes
    if command == "special":
        total_price -= total_price * 0.1
    print(f"Total price: {total_price:.2f}$")


