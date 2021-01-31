def password_check(pass_input):
    check_1 = False
    check_2 = False
    check_3 = False

    if len(pass_input) not in range(6, 11):
        check_1 = True

    number_of_digit = 0
    for element in pass_input:
        if ord(element) in range(48, 58):
            number_of_digit += 1

        if not element.isdigit() and not element.isalpha():
            check_2 = True
            break

    if number_of_digit < 2:
        check_3 = True

    return check_1, check_2, check_3


password = input()

check_list = password_check(password)
if check_list[0]:
    print("Password must be between 6 and 10 characters")
if check_list[1]:
    print("Password must consist only of letters and digits")
if check_list[2]:
    print("Password must have at least 2 digits")
if not check_list[0] and not check_list[1] and not check_list[2]:
    print("Password is valid")
