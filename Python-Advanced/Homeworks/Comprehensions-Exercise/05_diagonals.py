def read_row():
    return [int(el) for el in input().split(", ")]


size = int(input())
matrix = [read_row() for _ in range(size)]

first_diagonal = [matrix[index][index] for index in range(size)]
second_diagonal = [matrix[index][size - index - 1] for index in range(size)]

print(f"First diagonal: {', '.join([str(el) for el in first_diagonal])}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join([str(el) for el in second_diagonal])}. Sum: {sum(second_diagonal)}")
