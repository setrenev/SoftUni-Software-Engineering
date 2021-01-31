str_numbers = input().split()
remove_count = int(input())

numbers_list = []

for element in str_numbers:
    number = int(element)
    numbers_list.append(number)

for remove in range(remove_count):
    numbers_list.remove(min(numbers_list))

print(numbers_list)
