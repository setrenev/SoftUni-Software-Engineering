def jump_function(index, harts):
    if harts == 2:
        harts = 0
        print(f"Place {index} has Valentine's day.")
    elif harts == 0:
        print(f"Place {index} already had Valentine's day.")
    else:
        harts -= 2
    return harts


houses = [int(el) for el in input().split("@")]

position = 0

command = input()
while not command == "Love!":
    jump = int(command.split()[1])

    if position + jump < len(houses):
        position += jump
    else:
        position = 0

    houses[position] = jump_function(position, houses[position])
    command = input()

filed_houses = [el for el in houses if el > 0]

print(f"Cupid's last position was {position}.")

if len(filed_houses) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(filed_houses)} places.")
