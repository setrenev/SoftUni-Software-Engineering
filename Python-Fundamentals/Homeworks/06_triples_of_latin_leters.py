number = int(input())

for char_1 in range(97, 97 + number):
    for char_2 in range(97, 97 + number):
        for char_3 in range(97, 97 + number):
            print(f"{chr(char_1)}{chr(char_2)}{chr(char_3)}")