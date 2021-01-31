first_string, second_string = input().split()

total_sum = 0

for index in range(len(first_string) + len(second_string)):
    if index not in range(len(first_string)):
        x = 1
    else:
        x = ord(first_string[index])

    if index not in range(len(second_string)):
        y = 1
    else:
        y = ord(second_string[index])

    if x == 1 and y == 1:
        break

    total_sum += x * y


print(total_sum)
