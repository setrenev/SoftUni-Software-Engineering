word = input()

dict_word = {}

for el in word:
    if not el == " ":
        count = word.count(el)
        dict_word.update({el: count})

for key, value in dict_word.items():
    print(f"{key} -> {value}")
