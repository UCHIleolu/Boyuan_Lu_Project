# CarInventory
from Car import Car
from CarInventoryNode import CarInventoryNode

class CarInventory:
    def __init__(self):
        self.root = None

    def addCar(self, car):
        n = CarInventoryNode(car)

        if not self.root:
            self.root = n
        else:
            c = self.root

            while True:
                if car.make == c.getMake():
                    if car.model == c.getModel():
                        c.cars.append(car)
                        break
                    elif car.model < c.getModel():
                        if c.getLeft():
                            c = c.getLeft()
                        else:
                            c.setLeft(n)
                            break
                    else:
                        if c.getRight():
                            c = c.getRight()
                        else:
                            c.setRight(n)
                            break
                elif car.make < c.getMake():
                    if c.getLeft():
                        c = c.getLeft()
                    else:
                        c.setLeft(n)
                        break
                else:
                    if c.getRight():
                        c = c.getRight()
                    else:
                        c.setRight(n)
                        break


    def doesCarExist(self, car):
        current = self.root
        while current is not None:
            if car.make.upper() == current.getMake() and car.model.upper() == current.getModel():
                if car in current.cars:
                    return True
            if car > current.cars[-1]:
                current = current.right
            else:
                current = current.left
        return False
    

    def inOrder(self):
        result = ""
        stack = []
        current = self.root

        while current or stack:
            while current:
                stack.append(current)
                current = current.getLeft()

            if stack:
                current = stack.pop()
                result += str(current)
                current = current.getRight()

        return result
    
    def preOrder(self):
        return self.PO(self.root)

    def PO(self, CN):
        result = ""
        if CN:
            result += str(CN)
            result += self.PO(CN.left)
            result += self.PO(CN.right)
        return result

    def postOrder(self):
        return self.PsO(self.root)

    def PsO(self, CN):
        result = ""
        if CN:
            result += self.PsO(CN.left)
            result += self.PsO(CN.right)
            result += str(CN)
        return result
    
    def getBestCar(self, make, model):
        current = self.root
        Bcar = None
        while current is not None:
            if make.upper() == current.getMake() and model.upper() == current.getModel():
                for car in current.cars:
                    if Bcar is None or car > Bcar:
                        Bcar = car
            if make.upper() > current.getMake() or (make.upper() == current.getMake() and model.upper() > current.getModel()):
                current = current.right
            else:
                current = current.left
        return Bcar

    def getWorstCar(self, make, model):
        current = self.root
        Wcar = None
        while current is not None:
            if make.upper() == current.getMake() and model.upper() == current.getModel():
                for car in current.cars:
                    if Wcar is None or car < Wcar:
                        Wcar = car
            if make.upper() > current.getMake() or (make.upper() == current.getMake() and model.upper() > current.getModel()):
                current = current.right
            else:
                current = current.left
        return Wcar

    def getTotalInventoryPrice(self):
        total_price = 0
        current = self.root
        i = []
        while current is not None or len(i) > 0:
            while current is not None:
                i.append(current)
                current = current.left
            current = i.pop()
            for car in current.cars:
                total_price += car.price
            current = current.right
        return total_price


    def getSuccessor(self, make, model):
        current = self.root
        successor = None

        while current is not None:
            if make.upper() == current.getMake() and model.upper() == current.getModel():
                break
            elif make.upper() > current.getMake() or (make.upper() == current.getMake() and model.upper() > current.getModel()):
                current = current.right
            else:
                successor = current
                current = current.left

        if current is None:
            return None

        if current.right is not None:
            successor = current.right
            while successor.left is not None:
                successor = successor.left
        elif successor is None:
            return None

        return successor

    def removeCar(self, make, model, year, price):
        removecar = Car(make, model, year, price)

        current = self.root
        parent = None
        Lchild = False

        while current != None:
            if removecar.make == current.getMake() and removecar.model == current.getModel():

                if removecar in current.cars:

                    current.cars.remove(removecar)

                    if len(current.cars) == 0:
                        if current.left == None and current.right == None:
                            if parent == None:
                                self.root = None
                            elif Lchild:
                                parent.left = None
                            else:
                                parent.right = None
                                
                        elif current.left is None:
                            if parent is None:
                                self.root = current.right
                            elif Lchild:
                                parent.left = current.right
                            else:
                                parent.right = current.right
                                
                        elif current.right is None:
                            if parent is None:
                                self.root = current.left
                            elif Lchild:
                                parent.left = current.left
                            else:
                                parent.right = current.left
                                
                        else:
                            Psuccessor = current
                            successor = current.right

                            while successor.left != None:
                                Psuccessor = successor
                                successor = successor.left

                            current.make = successor.make
                            current.model = successor.model
                            current.cars = successor.cars

                            if Psuccessor.left == successor:
                                Psuccessor.left = successor.right
                            else:
                                Psuccessor.right = successor.right

                    return True

            parent = current
            if removecar.make > current.getMake() or (removecar.make == current.getMake() and removecar.model > current.getModel()):
                current = current.right
                Lchild = False
            else:
                current = current.left
                Lchild = True

        return False
