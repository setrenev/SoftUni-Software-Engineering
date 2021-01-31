line = input()

output = line[0]

for index in range(1, len(line)):
    if not line[index] == line[index-1]:
        output += line[index]

print(output)
