import re

data = input()

pattern = r"(^|(?<=\s))[a-z0-9]+[\._-]?[a-z0-9]+@[a-z]+[\-]?[a-z]+(\.[a-z]+)+\b"

emails = re.finditer(pattern, data, re.IGNORECASE)

[print(mail.group()) for mail in emails]
