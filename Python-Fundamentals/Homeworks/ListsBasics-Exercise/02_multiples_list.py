factor = int(input())
count = int(input())

created_list = []

for index in range(1, count + 1):
    created_list.append(index * factor)

print(created_list)
