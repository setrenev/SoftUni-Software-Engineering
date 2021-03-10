import re

data = input()
searched_word = input()

pattern = fr"\b{searched_word}\b"

find_word = re.findall(pattern, data, re.IGNORECASE)

print(len(find_word))
