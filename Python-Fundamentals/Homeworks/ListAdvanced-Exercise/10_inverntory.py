collecting_items = input().split(", ")

while True:
    command = input().split(" - ")
    type_of_command = command[0]

    if type_of_command == "Craft!":
        break

    item = command[1]

    if type_of_command == "Collect":
        if item not in collecting_items:
            collecting_items.append(item)
    elif type_of_command == "Drop":
        if item in collecting_items:
            collecting_items.remove(item)
    elif type_of_command == "Combine Items":
        combine = item.split(":")
        if combine[0] in collecting_items:
            find_position = collecting_items.index(combine[0])
            collecting_items.insert(find_position + 1, combine[1])
    elif type_of_command == "Renew":
        if item in collecting_items:
            collecting_items.remove(item)
            collecting_items.append(item)

print(", ".join(collecting_items))

