def add_func(places, i, string):
    if i in range(len(places)):
        result = places[:i] + string + places[i:]
    else:
        result = places
    print(result)
    return result


def remove_func(places, start_i, end_i):
    if start_i in range(len(places)) and end_i in range(len(places)):
        result = places[:start_i] + places[end_i+1:]
    else:
        result = places
    print(result)
    return result


def switch_func(places, old, new):
    if old in places:
        result = places.replace(old, new)
    else:
        result = places
    print(result)
    return result


stops = input()

line = input()

while not line == "Travel":
    command, addition_1, addition_2 = line.split(":")

    if command == "Add Stop":
        index = int(addition_1)
        string_to_add = addition_2
        stops = add_func(stops, index, string_to_add)

    elif command == "Remove Stop":
        start_index = int(addition_1)
        end_index = int(addition_2)
        stops = remove_func(stops, start_index, end_index)

    elif command == "Switch":
        old_string = addition_1
        new_string = addition_2
        stops = switch_func(stops, old_string, new_string)

    line = input()

print(f"Ready for world tour! Planned stops: {stops}")
