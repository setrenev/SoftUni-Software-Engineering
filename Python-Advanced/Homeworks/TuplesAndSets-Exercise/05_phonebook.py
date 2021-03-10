def searching(count, phone_b):
    for _ in range(count):
        contact_name = input()
        if contact_name not in phone_b:
            print(f"Contact {contact_name} does not exist.")
        else:
            print(f"{contact_name} -> {phone_b[contact_name]}")


contacts = {}

while True:
    line_data = input()
    if line_data[0].isalpha():
        name, phone_number = line_data.split("-")
        contacts[name] = phone_number
    else:
        n = int(line_data)
        break

searched_names = searching(n, contacts)
