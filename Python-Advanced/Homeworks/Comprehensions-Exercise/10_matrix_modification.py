def check_coordinates(size, r, c):
    if 0 <= r < size and 0 <= c < size:
        return True


size = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(size)]

while True:
    data = input()
    if data == "END":
        break

    line = data.split()
    command = line[0]
    row_index, col_index, value = [int(el) for el in line[1:]]

    if not check_coordinates(size, row_index, col_index):
        print("Invalid coordinates")
        continue

    if command == "Add":
        matrix[row_index][col_index] += value
    elif command == "Subtract":
        matrix[row_index][col_index] -= value

[print(*row, sep=" ") for row in matrix]
