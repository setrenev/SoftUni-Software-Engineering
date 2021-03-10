def revert_func(current_condition, km, current_car):
    new_mileage = current_condition["mileage"] - km
    if new_mileage >= 10000:
        current_condition["mileage"] = new_mileage
        print(f"{current_car} mileage decreased by {km} kilometers")
    else:
        current_condition["mileage"] = 10000
    return current_condition


def refuel_func(current_condition, to_fill, current_car):
    new_fuel_amount = current_condition["fuel"] + to_fill
    if new_fuel_amount <= 75:
        current_condition["fuel"] = new_fuel_amount
    else:
        to_fill = 75 - current_condition["fuel"]
        current_condition["fuel"] = 75

    print(f"{current_car} refueled with {to_fill} liters")
    return current_condition


def drive_func(current_condition, to_drive, needed_fuel, current_car):
    if current_condition["fuel"] < needed_fuel:
        print("Not enough fuel to make that ride")
    else:
        current_condition["fuel"] -= needed_fuel
        current_condition["mileage"] += to_drive
        print(f"{current_car} driven for {to_drive} kilometers. {needed_fuel} liters of fuel consumed.")

    return current_condition


cars = {}

n = int(input())

for _ in range(n):
    car, mileage, fuel = input().split("|")
    condition = {"mileage": int(mileage), "fuel": int(fuel)}
    cars[car] = condition

line = input()

while not line == "Stop":
    command_line = line.split(" : ")
    command = command_line[0]
    car = command_line[1]

    if command == "Drive":
        distance, fuel = command_line[2:4]
        cars[car] = drive_func(cars[car], int(distance), int(fuel), car)
        if cars[car]["mileage"] >= 100000:
            del cars[car]
            print(f"Time to sell the {car}!")

    elif command == "Refuel":
        fuel = int(command_line[2])
        cars[car] = refuel_func(cars[car], fuel, car)

    elif command == "Revert":
        kilometers = int(command_line[2])
        cars[car] = revert_func(cars[car], kilometers, car)

    line = input()

sorted_cars = sorted(cars.items(), key=lambda x: (-x[1]["mileage"], x[0]))
for car, value in sorted_cars:
    print(f"{car} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")
