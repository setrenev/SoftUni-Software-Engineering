list_of_numbers = [int(el) for el in input().split(", ")]

max_range = max(list_of_numbers)

for group in range(10, max_range + 10, 10):
    numbers_in_group = [element for element in list_of_numbers if element in range(group - 9, group + 1)]
    print(f"Group of {group}'s: {numbers_in_group}")
