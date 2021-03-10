def strike(targets, index, radius):
    left_targets = targets[:index]
    right_targets = targets[index + 1:]
    if radius in range(len(left_targets) + 1) and radius in range(len(right_targets) + 1):
        targets = left_targets[:len(left_targets) - radius] + right_targets[len(right_targets) - radius:]
    else:
        print("Strike missed!")

    return targets


targets_values = [int(element) for element in input().split()]

while True:
    command_line = input().split()
    command = command_line[0]
    if command == "End":
        break

    index_of_target = int(command_line[1])
    number = int(command_line[2])

    if command == "Shoot":
        if index_of_target in range(len(targets_values)):
            targets_values[index_of_target] -= number
            if targets_values[index_of_target] <= 0:
                targets_values.pop(index_of_target)
    elif command == "Add":
        if index_of_target in range(len(targets_values)):
            targets_values.insert(index_of_target, number)
        else:
            print("Invalid placement!")
    elif command == "Strike":
        targets_values = strike(targets_values, index_of_target, number)

targets_values = [str(target) for target in targets_values]
print("|".join(targets_values))
