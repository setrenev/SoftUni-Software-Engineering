def add_element(lst, mov):
    element = f"-{mov}a"
    mid_index = len(lst) // 2
    lst.insert(mid_index, element)
    lst.insert(mid_index, element)
    return lst


cards = [el for el in input().split()]

moves = 0
won = False

command = input()

while not command == "end":
    if len(cards) == 0:
        won = True
        break

    moves += 1
    first_index, second_index = [int(el) for el in command.split()]

    if first_index == second_index or first_index not in range(len(cards)) or second_index not in range(len(cards)):
        cards = add_element(cards, moves)
        print("Invalid input! Adding additional elements to the board")
    elif cards[first_index] == cards[second_index]:
        matching_element = cards[first_index]
        cards.remove(matching_element)
        cards.remove(matching_element)
        print(f"Congrats! You have found matching elements - {matching_element}!")
    elif not cards[first_index] == cards[second_index]:
        print("Try again!")

    command = input()

if len(cards) > 0:
    print("Sorry you lose :(")
    print(" ".join(str(element) for element in cards))

if won or len(cards) == 0:
    print(f"You have won in {moves} turns!")
