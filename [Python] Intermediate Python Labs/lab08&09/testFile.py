from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory

def test_car():
    car = Car("Ford", "Escape", 2023, 35000)
    assert car.make == "FORD"
    assert car.model == "ESCAPE"
    assert car.year == 2023
    assert car.price == 35000

def test_car_gt():
    car1 = Car("Ford", "Escape", 2022, 30000)
    car2 = Car("Tesla", "SModel", 2023, 35000)
    assert car2 > car1

def test_car_lt():
    car1 = Car("Ford", "Escape", 2022, 30000)
    car2 = Car("Tesla", "SModel", 2023, 35000)
    assert car1 < car2

def test_carinventorynode():
    car = Car("Ford", "Escape", 2023, 35000)
    node = CarInventoryNode(car)
    assert node.make == "FORD"
    assert node.model == "ESCAPE"
    assert node.cars == [car]
    assert node.parent is None
    assert node.left is None
    assert node.right is None

def test_carinventorynode_str():
    car1 = Car("Nissan", "Leaf", 2020, 30000)
    car2 = Car("Tesla", "SModel", 2022, 50000)
    node = CarInventoryNode(car1)
    node.cars.append(car2)
    expected_output = 'Make: NISSAN, Model: LEAF, Year: 2020, Price: $30000\nMake: TESLA, Model: SMODEL, Year: 2022, Price: $50000\n'
    assert str(node) == expected_output


def test_addCar():
    inventory = CarInventory()

    car1 = Car("Make1", "Model1", 2020, 20000)
    car2 = Car("Make2", "Model2", 2022, 30000)

    inventory.addCar(car1)
    inventory.addCar(car2)

    assert inventory.doesCarExist(car1) is True
    assert inventory.doesCarExist(car2) is True

def test_doesCarExist():
    inventory = CarInventory()

    car1 = Car("Make1", "Model1", 2021, 20000)
    car2 = Car("Make2", "Model2", 2022, 30000)
    car3 = Car("Make3", "Model3", 2023, 40000)

    inventory.addCar(car1)
    inventory.addCar(car2)

    assert inventory.doesCarExist(car1) is True
    assert inventory.doesCarExist(car2) is True
    assert inventory.doesCarExist(car3) is False

def test_inOrder():
    inventory = CarInventory()

    car1 = Car("Make1", "Model1", 2021, 20000)
    car2 = Car("Make2", "Model2", 2022, 30000)
    car3 = Car("Make3", "Model3", 2023, 30000)

    inventory.addCar(car1)
    inventory.addCar(car2)
    inventory.addCar(car3)

    expected_order = 'Make: MAKE1, Model: MODEL1, Year: 2021, Price: $20000\nMake: MAKE2, Model: MODEL2, Year: 2022, Price: $30000\nMake: MAKE3, Model: MODEL3, Year: 2023, Price: $30000\n'
    assert inventory.inOrder() == expected_order

def test_preOrder():
    inventory = CarInventory()

    car1 = Car("Make1", "Model1", 2021, 20000)
    car2 = Car("Make2", "Model2", 2022, 30000)
    car3 = Car("Make3", "Model3", 2023, 30000)

    inventory.addCar(car1)
    inventory.addCar(car2)
    inventory.addCar(car3)

    expected_order = 'Make: MAKE1, Model: MODEL1, Year: 2021, Price: $20000\nMake: MAKE2, Model: MODEL2, Year: 2022, Price: $30000\nMake: MAKE3, Model: MODEL3, Year: 2023, Price: $30000\n'
    assert inventory.preOrder() == expected_order

def test_postOrder():
    inventory = CarInventory()

    car1 = Car("Make1", "Model1", 2021, 20000)
    car2 = Car("Make2", "Model2", 2022, 30000)
    car3 = Car("Make3", "Model3", 2023, 30000)

    inventory.addCar(car1)
    inventory.addCar(car2)
    inventory.addCar(car3)

    expected_order = 'Make: MAKE3, Model: MODEL3, Year: 2023, Price: $30000\nMake: MAKE2, Model: MODEL2, Year: 2022, Price: $30000\nMake: MAKE1, Model: MODEL1, Year: 2021, Price: $20000\n'
    assert inventory.postOrder() == expected_order

def test_getBestCar():
    inventory = CarInventory()

    car1 = Car("Make1", "Model1", 2021, 20000)
    car2 = Car("Make1", "Model1", 2022, 30000)
    car3 = Car("Make1", "Model1", 2023, 30000)

    inventory.addCar(car1)
    inventory.addCar(car2)
    inventory.addCar(car3)

    best_car = inventory.getBestCar("Make1", "Model1")
    assert best_car == car3

def test_getWorstCar():
    inventory = CarInventory()

    car1 = Car("Make1", "Model1", 2021, 20000)
    car2 = Car("Make1", "Model1", 2022, 30000)
    car3 = Car("Make1", "Model1", 2023, 30000)

    inventory.addCar(car1)
    inventory.addCar(car2)
    inventory.addCar(car3)

    worst_car = inventory.getWorstCar("Make1", "Model1")
    assert worst_car == car1

def test_getTotalInventoryPrice():
    inventory = CarInventory()

    car1 = Car("Make1", "Model1", 2021, 20000)
    car2 = Car("Make2", "Model2", 2022, 30000)
    car3 = Car("Make3", "Model3", 2023, 30000)

    inventory.addCar(car1)
    inventory.addCar(car2)
    inventory.addCar(car3)

    expected_total_price = car1.price + car2.price + car3.price
    assert inventory.getTotalInventoryPrice() == expected_total_price

def test_getSuccessor():
    inventory = CarInventory()
    
    car1 = Car("Cars", "Model", 2020, 25000)
    car2 = Car("Car", "Models", 2018, 22000)
    car3 = Car("Cars", "Modelx", 2019, 18000)
    car4 = Car("Car", "Modelxs", 2021, 20000)
    car5 = Car("Cars", "Model", 2022, 28000)
    car6 = Car("Car", "Models", 2020, 24000)

    inventory.addCar(car1)
    inventory.addCar(car2)
    inventory.addCar(car3)
    inventory.addCar(car4)
    inventory.addCar(car5)
    inventory.addCar(car6)
    
    successor = inventory.getSuccessor("Cars", "Model")
    assert successor == car3
    
    successor = inventory.getSuccessor("Car", "Models")
    assert successor == car4
    
    successor = inventory.getSuccessor("Car", "Modelxs")
    assert successor == car1


def test_removeCar():
    inventory = CarInventory()
    car1 = Car("Make", "Model1", 2022, 25000)
    car2 = Car("Make", "Model2", 2023, 22000)
    car3 = Car("Make", "Model3", 2024, 28000)

    inventory.addCar(car1)
    inventory.addCar(car2)
    inventory.addCar(car3)

    # Case 1:
    assert inventory.removeCar("Make", "Model3", 2024, 28000) == True
    assert inventory.doesCarExist(car3) == False

    # Case 2:
    assert inventory.removeCar("Make", "Model2", 2023, 22000) == True
    assert inventory.doesCarExist(car2) == False

    # Case 3:
    assert inventory.removeCar("Make", "Model1", 2022, 25000) == True
    assert inventory.doesCarExist(car1) == False

    # Remove non-existing car
    assert inventory.removeCar("Ford", "Escape", 2022, 28000) == False
