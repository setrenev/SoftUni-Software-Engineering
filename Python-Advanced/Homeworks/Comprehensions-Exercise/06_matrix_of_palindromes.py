def get_palindrome(r, c):
    palindrome = ""
    palindrome += chr(97 + r)
    palindrome += chr(97 + r + c)
    palindrome += chr(97 + r)
    return palindrome


rows_count, cols_count = [int(el) for el in input().split()]

matrix = []

for row in range(rows_count):
    matrix.append([])
    for col in range(cols_count):
        matrix[row].append(get_palindrome(row, col))

[print(" ".join(el)) for el in matrix]
