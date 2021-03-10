first_list = input().split(", ")
second_list = input().split(", ")

result = []

for element_1 in first_list:
    for element_2 in second_list:
        if element_1 in element_2 and element_1 not in result:
            result.append(element_1)

print(result)
