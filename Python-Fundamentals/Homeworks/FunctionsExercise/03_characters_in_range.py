def resolve_function(char_1, char_2):
    for index in range(ord(char_1)+1, ord(char_2)):
        print(f"{chr(index)}",end=" ")


first_char = input()
second_char = input()

resolve_function(first_char, second_char)
