# usernames = [
#     "George",
#     "George",
#     "George",
#     "Peter",
#     "George",
#     "NiceGuy1234",
# ]


def input_to_list(count):
    line = []
    for _ in range(count):
        line.append(input())
    return line


def print_result(elements):
    for el in elements:
        print(el)


n = int(input())
usernames = input_to_list(n)
unique_usernames = set(usernames)
print_result(unique_usernames)
