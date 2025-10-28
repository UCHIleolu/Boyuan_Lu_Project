from Pizza import *
from CustomPizza import *
from SpecialtyPizza import *
from PizzaOrder import *
from OrderQueue import *
def test_Pizza():
    pizza = Pizza("M")
    assert pizza.getSize() == "M"
    assert pizza.getPrice() == 0.0

    pizza.setSize("L")
    pizza.setPrice(11.99)
    assert pizza.getSize() == "L"
    assert pizza.getPrice() == 11.99

def test_CustomPizza():
    cp = CustomPizza("S")
    assert cp.getSize() == "S"
    assert cp.getPrice() == 8.0

    cp.addTopping("extra cheese")
    cp.addTopping("sausage")
    assert cp.getPizzaDetails() == 'CUSTOM PIZZA\nSize: S\nToppings:\n\t+ extra cheese\n\t+ sausage\nPrice: $9.00\n'

def test_SpecialtyPizza():
    sp = SpecialtyPizza("L", "Spicy Chicken")
    assert sp.getSize() == "L"
    assert sp.getPrice() == 16.0

    assert sp.getPizzaDetails() == 'SPECIALTY PIZZA\nSize: L\nName: Spicy Chicken\nPrice: $16.00\n'

def test_PizzaOrder():
    PO = PizzaOrder(123456)
    assert PO.getTime() == 123456

    cp = CustomPizza("S")
    cp.addTopping("extra cheese")
    cp.addTopping("sausage")

    sp = SpecialtyPizza("S", "Creamy Mushroom")

    PO.addPizza(cp)
    PO.addPizza(sp)

    assert PO.getOrderDescription() == '******\nOrder Time: 123456\nCUSTOM PIZZA\nSize: S\nToppings:\n\t+ extra cheese\n\t+ sausage\nPrice: $9.00\n\n----\nSPECIALTY PIZZA\nSize: S\nName: Creamy Mushroom\nPrice: $12.00\n\n----\nTOTAL ORDER PRICE: $21.00\n******\n'

def test_OrderQueue():
    oq = OrderQueue()

    PO1 = PizzaOrder(90000)
    PO2 = PizzaOrder(100000)
    PO3 = PizzaOrder(110000)

    oq.addOrder(PO1)
    oq.addOrder(PO2)
    oq.addOrder(PO3)

    assert oq.processNextOrder() == PO1.getOrderDescription()
    assert oq.processNextOrder() == PO2.getOrderDescription()
    assert oq.processNextOrder() == PO3.getOrderDescription()
