import re

pattern = r"^@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+$"

count_barcodes = int(input())

for index in range(count_barcodes):
    product_group = "00"
    barcode = input()

    if not re.findall(pattern, barcode):
        print("Invalid barcode")
    else:
        match = re.findall(r"\d", barcode)
        if not len(match) == 0:
            product_group = ("".join(match))

        print(f"Product group: {product_group}")
