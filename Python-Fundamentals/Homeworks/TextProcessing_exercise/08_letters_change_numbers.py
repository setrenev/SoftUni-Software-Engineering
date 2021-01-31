def sum_string(first, second, num):
    sum_of_string = 0
    if ord(first) in range(65, 91):
        sum_of_string += num / (ord(first) - 64)
    else:
        sum_of_string += num * (ord(first) - 96)

    if ord(second) in range(65, 91):
        sum_of_string -= ord(second) - 64
    else:
        sum_of_string += ord(second) - 96

    return sum_of_string


strings = input().split()

total_sum = 0

for string in strings:
    first_letter = string[0]
    second_letter = string[-1]
    number = int(string[1:-1])
    total_sum += sum_string(first_letter, second_letter, number)

print(f"{total_sum:.2f}")