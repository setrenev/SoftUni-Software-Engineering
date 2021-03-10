# data = [
#     1,
#     3,
#     5,
#     7,
#     3,
#     4,
#     5,
# ]


def input_to_list(count):
    line = []
    for _ in range(count):
        line.append(input())
    return line


def print_result(elements):
    for el in elements:
        print(el)


n, m = [int(number) for number in input().split()]

first_part = input_to_list(n)
second_part = input_to_list(m)

unique_elements = set(first_part).intersection(set(second_part))
print_result(unique_elements)
