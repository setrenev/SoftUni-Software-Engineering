import re

data = input()
cool_threshold = 1

digits = re.findall(r"\d", data)
for digit in digits:
    cool_threshold *= int(digit)

pattern = r"([:]{2}[A-Z][a-z]{2,}[:]{2})|([*]{2}[A-Z][a-z]{2,}[*]{2})"
emojis = {}

found_emojis = re.finditer(pattern, data)

for element in found_emojis:
    emoji = element.group()
    coolness = 0
    for index in range(2, len(emoji)-2):
        coolness += ord(emoji[index])
    emojis[emoji] = coolness

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for key, value in emojis.items():
    if value > cool_threshold:
        print(key)
