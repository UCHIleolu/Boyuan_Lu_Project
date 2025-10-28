#Beverage
class Beverage:
    def __init__(self, ounces, price):
        self.ounces = ounces
        self.price = price

    def updateOunces(self, ounces):
        self.ounces = ounces

    def updatePrice(self, price):
        self.price = price

    def getOunces(self):
        return self.ounces

    def getPrice(self):
        return self.price

    def getInfo(self):
        return "{} oz, ${:.2f}".format(self.ounces,self.price)
