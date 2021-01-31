class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product):
        if len(self.storage) < self.capacity:
            self.storage.append(product)

    def get_products(self):
        return self.storage


storage = Storage(int(input()))

while True:
    product = input()
    if product == "End":
        break
    storage.add_product(product)

print(storage.get_products())
