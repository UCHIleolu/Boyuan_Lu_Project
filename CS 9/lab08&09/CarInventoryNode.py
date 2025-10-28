# CarInventoryNode
from Car import Car

class CarInventoryNode:
    def __init__(self, car):
        self.make = car.make.upper()
        self.model = car.model.upper()
        self.year = car.year
        self.price = car.price
        self.cars = [car]
        self.parent = None
        self.left = None
        self.right = None

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getYear(self):
        return self.year

    def getPrice(self):
        return self.price

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def __str__(self):
        result = ""
        for i in self.cars:
            result += str(i) + "\n"
        return result
