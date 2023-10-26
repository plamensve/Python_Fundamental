class Inventory:
    items = []

    def __init__(self, capacity):
        self._capacity = capacity
        self.cap = capacity

    def add_item(self, item: str):
        if self.cap > 0:
            self.cap -= 1
            Inventory.items.append(item)
        else:
            return "Not enough room in the inventory"

    def get_capacity(self):
        return self._capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.cap}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
