def factorial_calc(num):
    result = 1
    for element in range(2, num+1):
        result *= element
    return result


number_one = int(input())
number_two = int(input())

factorial_number_one = factorial_calc(number_one)
factorial_number_two = factorial_calc(number_two)

result_output = factorial_number_one / factorial_number_two
print(f"{result_output:.2f}")
