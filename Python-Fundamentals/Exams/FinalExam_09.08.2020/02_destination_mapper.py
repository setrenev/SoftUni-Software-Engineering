import re

pattern = r"((?<=\=)[A-Z][A-Za-z]{2,}(?=\=))|((?<=\/)[A-Z][A-Za-z]{2,}(?=\/))"
valid_places = []
travel_points = 0

line = input()

match = re.finditer(pattern, line)

for el in match:
    place = el.group()
    valid_places.append(place)

for place in valid_places:
    travel_points += len(place)

print("Destinations: ", end="")
print(", ".join(valid_places))
print(f"Travel Points: {travel_points}")
