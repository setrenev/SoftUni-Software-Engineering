class Inventory:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []
        self.left_capacity = capacity

    def get_capacity(self):
        return self.__capacity

    def add_item(self, item):
        if len(self.items) < self.__capacity:
            self.items.append(item)
            self.left_capacity -= 1
        else:
            return "not enough room in the inventory"

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.left_capacity}"


inventory = Inventory(10)
inventory.add_item("potion")
inventory.add_item("sword")
inventory.add_item("bottle")
print(inventory.get_capacity())
print(inventory)
