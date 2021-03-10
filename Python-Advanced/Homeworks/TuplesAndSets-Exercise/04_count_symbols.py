def function_occurrences(txt):
    dict_of_counts = {}
    for character in txt:
        if character not in dict_of_counts:
            dict_of_counts[character] = 1
        else:
            dict_of_counts[character] += 1

    return dict_of_counts


def print_result(elements):
    for (key, value) in sorted(elements.items(), key=lambda x: x[0]):
        print(f"{key}: {value} time/s")


text = input()

#text = "SoftUni rocks"

occurrences = function_occurrences(text)
print_result(occurrences)
