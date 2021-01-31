CAPACITY = 255
total_litres = 0

pour_count = int(input())

for pour in range(pour_count):
    current_litres = int(input())
    if current_litres + total_litres > CAPACITY:
        print("Insufficient capacity!")
        continue
    total_litres += current_litres

print(total_litres)
