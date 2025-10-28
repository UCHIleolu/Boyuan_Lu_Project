#testFile
from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
from DrinkOrder import DrinkOrder

#test Beverage.py
def test_beverage1():
    b1 = Beverage(1, 2.5)
    assert b1.getOunces() == 1
    assert b1.getPrice() == 2.5
    assert b1.getInfo() == '1 oz, $2.50'

def test_beverage2():
    b2 = Beverage(2, 3.4)
    b2.updateOunces(1)
    assert b2.getOunces() == 1
    b2.updatePrice(5)
    assert b2.getPrice() == 5
    assert b2.getInfo() == '1 oz, $5.00'

#test Coffee.py
def test_coffee1():
    c1 = Coffee(5, 3.4, "Latte")
    assert c1.getInfo() == 'Latte Coffee, 5 oz, $3.40'

def test_coffee2():
    c2 = Coffee(7, 10.5, "Mocha")
    assert c2.getInfo() == 'Mocha Coffee, 7 oz, $10.50'

#test FruitJuice.py
def test_fruitjuice1():
    f1 = FruitJuice(20, 5, ["Apple"])
    assert f1.getInfo() == 'Apple Juice, 20 oz, $5.00'

def test_fruitjuice2():
    f2 = FruitJuice(10, 3, ["Banana", "Mango"])
    assert f2.getInfo() == 'Banana/Mango Juice, 10 oz, $3.00'

def test_fruitjuice3():
    f3 = FruitJuice(30, 15, ["Pineapple", "Mango", "Passion fruit"])
    assert f3.getInfo() == 'Pineapple/Mango/Passion fruit Juice, 30 oz, $15.00'
    
#test DrinkOrder.py
def test_drinkorder1():
    d1 = DrinkOrder()
    assert d1.getTotalOrder() == 'Order Items:\nTotal Price: $0.00'

def test_drinkorder2():
    c2 = Coffee(7, 10.5, "Mocha")
    f2 = FruitJuice(10, 3, ["Banana", "Mango"])
    d2 = DrinkOrder()
    d2.addBeverage(c2)
    assert d2.getTotalOrder() == 'Order Items:\n* Mocha Coffee, 7 oz, $10.50\nTotal Price: $10.50'
    d2.addBeverage(f2)
    assert d2.getTotalOrder() =='Order Items:\n* Mocha Coffee, 7 oz, $10.50\n* Banana/Mango Juice, 10 oz, $3.00\nTotal Price: $13.50'
    

