def sum_numbers(n1, n2):
    return n1 + n2


def subtract(n3, sum_of_first_two):
    return sum_of_first_two - n3


def add_and_subtract(n1, n2, n3):
    sum_of_first_two = sum_numbers(n1, n2)
    return subtract(n3, sum_of_first_two)


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(add_and_subtract(number_1, number_2, number_3))
