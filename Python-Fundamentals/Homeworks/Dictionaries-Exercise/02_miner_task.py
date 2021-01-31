produce = {}

command = input()
key = ""
value = 0

while not command == "stop":
    key = command
    value = int(input())
    if key not in produce:
        produce[key] = value
    else:
        produce[key] += value

    command = input()

for resource, quantity in produce.items():
    print(f"{resource} -> {quantity}")
