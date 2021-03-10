import re

pattern = r"(#|\|)(?P<item>[A-Za-z\ ]+)\1(?P<date>[0-3][0-9]\/[0-1][0-9]\/[0-9][0-9])\1" \
          r"(?P<calories>0|([0-9]{1,4})|10000)\1"
foods = []
total_calories = 0

line = input()
match = re.finditer(pattern, line)

for m in match:
    foods.append(m.groupdict())
    total_calories += int(m["calories"])

print(f"You have food to last you for: {total_calories // 2000} days!")
for el in foods:
    print(f"Item: {el['item']}, Best before: {el['date']}, Nutrition: {el['calories']}")
