line = input().split(">")

output = line[0]
strength = 0
element = ""

for index in range(1, len(line)):
    strength += int(line[index][0])
    element = ">" + line[index]

    while strength > 0 and len(element) > 1:
        strength -= 1
        element = element.replace(element[1], "", 1)

    output += element

print(output)