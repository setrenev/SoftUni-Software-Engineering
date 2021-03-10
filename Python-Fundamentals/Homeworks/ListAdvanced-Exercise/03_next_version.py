software_version = [int(el) for el in input().split(".")]

for index in range(2, -1, -1):
    if software_version[index] == 9:
        software_version[index] = 0
    else:
        software_version[index] += 1
        break

new_version = ".".join(str(element) for element in software_version)

print(new_version)
