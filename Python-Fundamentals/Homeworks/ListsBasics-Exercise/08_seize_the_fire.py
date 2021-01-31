fire_cells = input().split("#")
water_amount = int(input())

current = []
value_of_cell = 0
effort = 0
total_fire = []

for cell in fire_cells:
    current = cell.split(" = ")
    value_of_cell = int(current[1])

    if water_amount < value_of_cell:
        continue

    if current[0] == "High" and value_of_cell in range(81, 126):
        water_amount -= value_of_cell
        effort += value_of_cell * 0.25
        total_fire.append(value_of_cell)

    elif current[0] == "Medium" and value_of_cell in range(51, 81):
        water_amount -= value_of_cell
        effort += value_of_cell * 0.25
        total_fire.append(value_of_cell)

    elif current[0] == "Low" and value_of_cell in range(1, 51):
        water_amount -= value_of_cell
        effort += value_of_cell * 0.25
        total_fire.append(value_of_cell)

print("Cells:")
for fire in total_fire:
    print(f" - {fire}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(total_fire)}")
