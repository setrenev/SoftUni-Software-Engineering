import re

pattern = r"(^|(?<=\s))w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+"

line = input()

while line:
    link = re.finditer(pattern, line)
    valid = [el.group() for el in link]
    if valid:
        print(*valid)

    line = input()
