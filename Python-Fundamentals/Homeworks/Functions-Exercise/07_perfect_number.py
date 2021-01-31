def perfect_number(num):
    divisors = []
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            divisors.append(i)

    result = sum(divisors)
    return result


number = int(input())

sum_of_divisors = perfect_number(number)
if sum_of_divisors == number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
