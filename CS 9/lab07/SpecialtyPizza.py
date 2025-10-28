# SpecialtyPizza
from Pizza import Pizza

class SpecialtyPizza(Pizza):
    def __init__(self, size, name):
        super().__init__(size)
        self.name = name
        if self.size == "S":
            self.price = 12.0
        elif self.size == "M":
            self.price = 14.0
        else:
            self.price = 16.0

    def getPizzaDetails(self):
        return f"SPECIALTY PIZZA\nSize: {self.size}\nName: {self.name}\nPrice: ${self.price:.2f}\n"
