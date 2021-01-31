characters_count = int(input())

result = 0

for char in range(characters_count):
    character = input()
    result += ord(character)

print(f"The sum equals: {result}")