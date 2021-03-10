line = [el for el in input().split("|")]
stack = [el.split() for el in line]

while stack:
    element = stack.pop()
    if element:
        print(*element, end=" ")
