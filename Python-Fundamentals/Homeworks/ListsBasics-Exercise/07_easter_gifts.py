gifts_name = input().split()

while True:
    command_list = input().split()

    if command_list == ["No", "Money"]:
        break

    elif "OutOfStock" in command_list:
        for index in range(len(gifts_name)):
            if gifts_name[index] == command_list[1]:
                gifts_name[index] = None

    elif "Required" in command_list:
        replace_index = int(command_list[2])
        if 0 <= replace_index < len(gifts_name):
            gifts_name[replace_index] = command_list[1]

    elif "JustInCase" in command_list:
        gifts_name[-1] = command_list[1]

for gift in gifts_name:
    if gift is not None:
        print(gift, end=" ")
