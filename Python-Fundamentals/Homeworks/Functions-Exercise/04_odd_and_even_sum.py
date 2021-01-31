def function_resolve(even_sum, odd_sum, num):
    for index in num:
        if int(index) % 2 == 0:
            even_sum += int(index)
        else:
            odd_sum += int(index)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()

print(function_resolve(0, 0, number))
