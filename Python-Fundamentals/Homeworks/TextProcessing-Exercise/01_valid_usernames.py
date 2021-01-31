def check_symbols(password):
    if password.replace("-", "").isidentifier():
        return True


passwords = input().split(", ")

for element in passwords:
    if len(element) in range(3, 17) and check_symbols(element):
        print(element)
