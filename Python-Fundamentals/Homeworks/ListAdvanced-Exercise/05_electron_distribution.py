electron_count = int(input())

electron_matrix = [int(2 * ((i + 1) ** 2)) for i in range(electron_count // 2)]

distribution = []

for element in electron_matrix:
    if element < electron_count:
        distribution.append(element)
        electron_count -= element
    elif element > electron_count:
        distribution.append(electron_count)
        break
    else:
        distribution.append(element)
        break

print(distribution)

# Variant 2
# electron_distribution = []
# position = 1
#
# while True:
#     count_electrons_in_position = 2 * (position ** 2)
#
#     if electron_count == 0:
#         break
#
#     if count_electrons_in_position <= electron_count:
#         electron_distribution.append(count_electrons_in_position)
#         electron_count -= count_electrons_in_position
#     else:
#         electron_distribution.append(count_electrons_in_position - electron_count)
#         break
#
#     position += 1
#
# print(electron_distribution)


