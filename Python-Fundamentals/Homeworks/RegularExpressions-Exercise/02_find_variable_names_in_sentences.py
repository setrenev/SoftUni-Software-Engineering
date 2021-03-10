import re

data = input()

pattern = r"((?<=^_)|(?<=\s_))[a-z0-9]+\b"

valid_names = re.finditer(pattern, data, re.IGNORECASE)

valid_names = [el.group() for el in valid_names]
print(",".join(valid_names))