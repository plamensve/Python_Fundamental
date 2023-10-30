class Vehicle:
    owner = False

    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price

    def buy(self, money: int, owner: str):
        if self.price <= money and self.owner is None:
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {money - self.price}"
        elif self.price > money:
            return "Sorry, not enough money"
        elif self.owner is not None:
            return "Car already sold"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"
