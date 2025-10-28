from Pizza import Pizza

class CustomPizza(Pizza):
    def __init__(self, size):
        super().__init__(size)
        self.toppings = []
        if self.size == "S":
            self.price += 8.00
        elif self.size == "M":
            self.price += 10.00
        elif self.size == "L":
            self.price += 12.00

    def addTopping(self, topping):
        self.toppings.append(topping)
        if self.size == "S":
            self.price += 0.50
        elif self.size == "M":
            self.price += 0.75
        elif self.size == "L":
            self.price += 1.00

    def getPizzaDetails(self):
        toppings = ""
        for i in self.toppings:
            toppings += "\t+ " + i + "\n"
        return f"CUSTOM PIZZA\nSize: {self.size}\nToppings:\n{toppings}Price: ${self.price:.2f}\n"
