items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}

key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
material = ""

while True:
    line = input().split()
    mark = False
    for index in range(0, len(line), 2):
        qty = int(line[index])
        material = line[index+1].lower()
        if material in key_materials:
            key_materials[material] += qty
            if key_materials[material] >= 250:
                key_materials[material] -= 250
                mark = True
                break
        elif material in junk:
            junk[material] += qty
        else:
            junk[material] = qty

    if mark:
        print(f"{items.get(material)} obtained!")
        break

for material, qty in sorted(key_materials.items(), key=lambda x: (-x[1], x[0])):
    print(f"{material}: {qty}")

for material, qty in sorted(junk.items()):
    print(f"{material}: {qty}")
