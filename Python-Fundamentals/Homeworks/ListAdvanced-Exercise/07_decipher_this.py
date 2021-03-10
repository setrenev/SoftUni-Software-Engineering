def decode_word(word):
    check_digits = [word[i] for i in range(len(word)) if word[i].isdigit()]
    first_letter = chr(int("".join(check_digits)))
    rest_of_word = "".join([word[i] for i in range(len(word)) if word[i].isalpha()])
    decipher_word = first_letter + rest_of_word[-1] + rest_of_word[1:-1]
    if len(rest_of_word) > 1:
        decipher_word += rest_of_word[0]

    return decipher_word


message = input().split()

decipher_list = [decode_word(element) for element in message]

decipher_message = " ".join(decipher_list)
print(decipher_message)
