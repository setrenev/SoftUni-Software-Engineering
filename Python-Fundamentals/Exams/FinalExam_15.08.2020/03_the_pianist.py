pieces = {}

n = int(input())

for _ in range(n):
    piece, composer, key = input().split("|")
    pieces.update({piece: {"composer": composer, "key": key}})

line = input()

while not line == "Stop":
    is_exist = False
    command_line = line.split("|")
    command = command_line[0]
    piece = command_line[1]
    if piece in pieces:
        is_exist = True

    if command == "Add":
        composer = command_line[2]
        key = command_line[3]
        if is_exist:
            print(f"{piece} is already in the collection!")
        else:
            pieces.update({piece: {"composer": composer, "key": key}})
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif command == "Remove":
        if is_exist:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command == "ChangeKey":
        new_key = command_line[2]
        if is_exist:
            pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    line = input()

sorted_pieces = sorted(pieces.items(), key=lambda x: (x[0], x[1]["composer"]))

for piece, composer_and_key in sorted_pieces:
    print(f"{piece} -> Composer: {composer_and_key['composer']}, Key: {composer_and_key['key']}")
