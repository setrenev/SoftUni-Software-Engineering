def function_resolve(num):
    if num[::-1] == num:
        return True
    else:
        return False


numbers_list = input().split(", ")

for element in numbers_list:
    print(function_resolve(element))
