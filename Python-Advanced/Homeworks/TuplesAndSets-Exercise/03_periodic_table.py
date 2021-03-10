def input_to_list(count):
    line = []
    for _ in range(count):
        line.append(input())
    return line


def split_elements(ch_el):
    elements = []
    for el in ch_el:
        if " " in el:
            sublist = el.split()
            [elements.append(x) for x in sublist]
        else:
            elements.append(el)

    return elements


def print_result(elements):
    for el in elements:
        print(el)


n = int(input())

chemical_elements = input_to_list(n)
unique_elements = set(split_elements(chemical_elements))
print_result(unique_elements)
