def insert_function(current, ind):
    processed = current[:ind] + " " + current[ind:]
    print(processed)
    return processed


def reverse_function(current, subs):
    processed = current
    if subs not in current:
        print("error")
    else:
        processed = current.replace(subs, "", 1)
        subs = subs[::-1]
        processed += subs
        print(processed)
    return processed


def change_function(current, subs, add_text):
    processed = current
    if subs in current:
        processed = current.replace(subs, add_text)
        print(processed)
    return processed


message = input()
line = input()

while not line == "Reveal":
    command = line.split(":|:")

    if command[0] == "InsertSpace":
        index = int(command[1])
        message = insert_function(message, index)

    elif command[0] == "Reverse":
        substring = command[1]
        message = reverse_function(message, substring)

    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = change_function(message, substring, replacement)

    line = input()

print(f"You have a new text message: {message}")
