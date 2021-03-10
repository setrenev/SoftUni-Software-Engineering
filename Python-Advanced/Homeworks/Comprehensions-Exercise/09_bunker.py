def print_items(data):
    category_items = []
    for product in data:                         # product is dictionary with one element
        category_items.append((*product,)[0])    # unpack dictionary, get key and append it to list
    return ", ".join(category_items)


def get_properties(data):
    data_1, data_2 = data.split(";")
    qty = int(data_1.split(":")[1])
    qlty = int(data_2.split(":")[1])
    return qty, qlty


bunker = {}
items_count = 0
total_quality = 0

[bunker.update({category: []}) for category in input().split(", ")]

n = int(input())

for _ in range(n):
    category, item, item_properties = input().split(" - ")
    properties = get_properties(item_properties)
    items_count += properties[0]
    total_quality += properties[1]
    bunker[category].append({item: list(properties)})

print(f"Count of items: {items_count}")
print(f"Average quality: {total_quality/len(bunker):.2f}")
[print(f"{category} -> {print_items(products)}") for category, products in bunker.items()]
