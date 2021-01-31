import sys
max_number = -sys.maxsize
min_number = sys.maxsize


def exchange_function(ind, list_n):
    if ind in range(len(list_n)):
        result = list_n[ind+1:] + list_n[:ind+1]
        return result
    else:
        print("Invalid index")


def max_even_function(list_n, max_n):
    result = None
    for i in range(len(list_n)):
        if list_n[i] % 2 == 0 and list_n[i] >= max_n:
            max_n = list_n[i]
            result = i

    return result


def max_odd_function(list_n, max_n):
    result = None
    for i in range(len(list_n)):
        if not list_n[i] % 2 == 0 and list_n[i] >= max_n:
            max_n = list_n[i]
            result = i

    return result


def min_even_function(list_n, min_n):
    result = None
    for i in range(len(list_n)):
        if list_n[i] % 2 == 0 and list_n[i] <= min_n:
            min_n = list_n[i]
            result = i
    return result


def min_odd_function(list_n, min_n):
    result = None
    for i in range(len(list_n)):
        if not list_n[i] % 2 == 0 and list_n[i] <= min_n:
            min_n = list_n[i]
            result = i
    return result


def first_count_elements(n_elements, type_n, list_n):
    result = []
    for i in range(n_elements):
        if type_n == "even" and list_n[i] % 2 == 0:
            result.append(list_n[i])
        elif type_n == "odd" and not list_n[i] % 2 == 0:
            result.append(list_n[i])
    return result


string_of_numbers = input().split(" ")

list_of_numbers = list(map(int, string_of_numbers))

while True:
    command_line = input().split(" ")
    if command_line[0] == "end":
        break
    elif command_line[0] == "exchange":
        index = int(command_line[1])
        list_of_numbers = exchange_function(index, list_of_numbers)
    elif command_line[0] == "max" and command_line[1] == "even":
        print(max_even_function(list_of_numbers, max_number))
    elif command_line[0] == "max" and command_line[1] == "odd":
        print(max_odd_function(list_of_numbers, max_number))
    elif command_line[0] == "min" and command_line[1] == "even":
        print(min_even_function(list_of_numbers, min_number))
    elif command_line[0] == "min" and command_line[1] == "odd":
        print(min_odd_function(list_of_numbers, min_number))
    elif command_line[0] == "first":
        count = int(command_line[1])
        type_of_elements = command_line[2]
        print(first_count_elements(count, type_of_elements, list_of_numbers))

