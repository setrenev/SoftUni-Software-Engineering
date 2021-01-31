line = input().upper()

substring = ""
number = ""
string = ""

index = 0
while index < len(line):
    if not line[index].isdigit():
        substring += line[index]
        index += 1
        continue

    while index < len(line) and line[index].isdigit():
        number += line[index]
        index += 1

    number = int(number)
    string += substring * number
    number = ""
    substring = ""

print(f"Unique symbols used: {len(set(string))}")
print(string)
