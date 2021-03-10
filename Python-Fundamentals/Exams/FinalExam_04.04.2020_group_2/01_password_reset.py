def take_odd_func(r_pass):
    new_pass = ""
    for ind in range(len(r_pass)):
        if not ind % 2 == 0:
            new_pass += r_pass[ind]
    return new_pass


def cut_func(r_pass, ind, long):
    new_pass = r_pass[:ind] + r_pass[ind+long:]
    return new_pass


def substitute_func(r_pass, searched, new_str):
    new_pass = r_pass
    if searched not in r_pass:
        print("Nothing to replace!")
    else:
        new_pass = r_pass.replace(searched, new_str)
        print(new_pass)
    return new_pass


raw_password = input()
line = input()

while not line == "Done":
    command = line.split()
    command_type = command[0]

    if command_type == "TakeOdd":
        raw_password = take_odd_func(raw_password)
        print(raw_password)
    elif command_type == "Cut":
        index = int(command[1])
        length = int(command[2])
        raw_password = cut_func(raw_password, index, length)
        print(raw_password)
    elif command_type == "Substitute":
        substring = command[1]
        substitute = command[2]
        raw_password = substitute_func(raw_password, substring, substitute)

    line = input()

print(f"Your password is: {raw_password}")