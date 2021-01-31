string_of_numbers = input().split(", ")
beggars_count = int(input())

list_of_numbers = []
result = []
index = 0

for num_el in string_of_numbers:
    number = int(num_el)
    list_of_numbers.append(number)

for element in range(beggars_count):
    result.append(0)

for num in list_of_numbers:
    result[index] += num
    index += 1
    if index == beggars_count:
        index = 0

print(result)
