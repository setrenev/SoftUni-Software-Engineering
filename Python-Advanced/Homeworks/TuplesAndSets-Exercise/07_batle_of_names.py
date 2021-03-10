odd_numbers = set()
even_numbers = set()

n = int(input())

for line in range(1, n+1):
    name = input()
    devised_number = sum([ord(character) for character in name]) // line

    if devised_number % 2 == 0:
        even_numbers.add(devised_number)
    else:
        odd_numbers.add(devised_number)

sum_of_odd_numbers = sum(odd_numbers)
sum_of_even_numbers = sum(even_numbers)

if sum_of_odd_numbers == sum_of_even_numbers:
    print(", ".join([str(el) for el in odd_numbers.union(even_numbers)]))
elif sum_of_odd_numbers > sum_of_even_numbers:
    print(", ".join([str(el) for el in odd_numbers.difference(even_numbers)]))
else:
    print(", ".join([str(el) for el in odd_numbers.symmetric_difference(even_numbers)]))
