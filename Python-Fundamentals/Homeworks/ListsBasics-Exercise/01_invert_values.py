string_input = input()

list_made = string_input.split()
final_list = []

for element in list_made:
    element = -1 * int(element)
    final_list.append(element)

print(final_list)
