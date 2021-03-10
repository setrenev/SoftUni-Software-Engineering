def is_even(word):
    if len(word) % 2 == 0:
        return True


words = input().split()

even_words = [print(word) for word in words if is_even(word)]
