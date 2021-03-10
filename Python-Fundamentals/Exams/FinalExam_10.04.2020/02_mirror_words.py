import re

pattern = r"((?<=#)([a-zA-Z]{3,})##([a-zA-Z]{3,})(?=#))|((?<=@)([a-zA-Z]{3,})@@([a-zA-Z]{3,})(?=@))"

word_pairs = []
valid_pairs = []

line = input()

match = re.finditer(pattern, line)
match = [el.group() for el in match]

for element in match:
    if "##" in element:
        pair = element.split("##")
    else:
        pair = element.split("@@")

    word_pairs.append(pair)

count_of_pairs = len(word_pairs)

for words in word_pairs:
    if words[0] == words[1][::-1]:
        valid_pairs.append(words)

if count_of_pairs == 0:
    print("No word pairs found!")
else:
    print(f"{count_of_pairs} word pairs found!")

if len(valid_pairs) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    for index in range(len(valid_pairs)):
        pair = " <=> ".join(valid_pairs[index])
        if not index == len(valid_pairs) - 1:
            print(f"{pair}, ", end="")
            continue
        print(f"{pair}")
