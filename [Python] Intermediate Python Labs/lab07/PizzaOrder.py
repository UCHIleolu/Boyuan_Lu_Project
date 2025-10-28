# PizzaOrder
from Pizza import *
from CustomPizza import *
from SpecialtyPizza import *
class PizzaOrder:
    def __init__(self, time):
        self.pizzas = []
        self.time = time

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getOrderDescription(self):
        orders = "******\nOrder Time: {}\n".format(self.time)
        TP = 0.0

        for i in self.pizzas:
            pizzas = i.getPizzaDetails()
            TP += i.getPrice()
            orders += pizzas + "\n----\n"

        orders += "TOTAL ORDER PRICE: ${:.2f}\n******\n".format(TP)
        return orders
