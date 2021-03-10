def correct_function(command_line, item_list, old_item):
    new_item = command_line[2]
    if old_item in item_list and new_item not in item_list:
        item_list = [new_item if el == old_item else el for el in item_list]
    return item_list


items = input().split("!")

while True:
    command = input().split()
    command_type = command[0]
    item = command[1]

    if command_type == "Go":
        break
    elif command_type == "Urgent" and item not in items:
        items.insert(0, item)
    elif command_type == "Unnecessary" and item in items:
        items.remove(item)
    elif command_type == "Correct":
        items = correct_function(command, items, item)
    elif command_type == "Rearrange" and item in items:
        items.remove(item)
        items.append(item)

print(", ".join(items))
