def smallest_number(num_list):
    min_number = min(num_list)
    return min_number


number_list = []
for index in range(3):
    number_list.append(int(input()))

print(smallest_number(number_list))
