#DrinkOrder
from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
class DrinkOrder:
    def __init__(self):
        self.drinks = []

    def addBeverage(self, beverage):
        self.drinks.append(beverage)

    def getTotalOrder(self):
        order=""
        order += "Order Items:\n"
        total = 0.00
        for i in self.drinks:
            order += f"* {i.getInfo()}\n"
            total += i.getPrice()
        order += f"Total Price: ${total:.2f}"
        return order
