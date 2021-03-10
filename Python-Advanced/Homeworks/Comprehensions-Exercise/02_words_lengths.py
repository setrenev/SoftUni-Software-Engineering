def print_word(words, i, count):
    print(f"{words[i]} -> {len(words[i])}", end="")
    if i < count-1:
        print(", ", end="")


data = input().split(", ")

word_count = len(data)

[print_word(data, index, word_count) for index in range(word_count)]
