def check_key(key_to_check, searched_str):
    if searched_str in key_to_check:
        print(f"{key_to_check} contains {searched_str}")
    else:
        print("Substring not found!")


def slice_key(key_to_slice, first, second):
    key_to_slice = key_to_slice[:first] + key_to_slice[second:]
    return key_to_slice


def change_key(key_to_change, command, first, second):
    medium_half = key_to_change[first:second]
    first_half = key_to_change[:first]
    end_half = key_to_change[second:]

    if command == "Upper":
        medium_half = medium_half.upper()
    elif command == "Lower":
        medium_half = medium_half.lower()

    key_to_change = first_half + medium_half + end_half
    return key_to_change


activation_key = input()

line = input()
while not line == "Generate":
    to_do = line.split(">>>")

    if to_do[0] == "Contains":
        substring = to_do[1]
        check_key(activation_key, substring)

    elif to_do[0] == "Flip":
        command_type = to_do[1]
        start_index = int(to_do[2])
        end_index = int(to_do[3])
        activation_key = change_key(activation_key, command_type, start_index, end_index)
        print(activation_key)

    elif to_do[0] == "Slice":
        start_index = int(to_do[1])
        end_index = int(to_do[2])
        activation_key = slice_key(activation_key, start_index, end_index)
        print(activation_key)

    line = input()

print(f"Your activation key is: {activation_key}")
