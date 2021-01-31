n = int(input())

parking_lot = {}

for index in range(n):
    data = input()
    command = data.split()[0]
    name = data.split()[1]

    if command == "register":
        plate_number = data.split()[2]
        if name not in parking_lot:
            parking_lot[name] = plate_number
            print(f"{name} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")
    else:
        if name in parking_lot:
            parking_lot.pop(name)
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for name, plate_number in parking_lot.items():
    print(f"{name} => {plate_number}")
