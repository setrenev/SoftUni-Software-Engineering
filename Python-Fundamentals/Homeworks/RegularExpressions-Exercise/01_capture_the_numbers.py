import re

data = ""
line = input()

while line:
    data += line
    line = input()

pattern = r"\d+"
numbers = re.findall(pattern, data)
print(*numbers)
