#Animal
class Animal:
    def __init__(self, species=None, weight=None, age=None, name=None):
        if species != None:
            self.species = species.upper()
        else:
            self.species = species
        self.weight = weight
        self.age = age
        if name != None:
            self.name = name.upper()
        else:
            self.name = name

    def setSpecies(self, species):
        self.species = species.upper()

    def setWeight(self, weight):
        self.weight = weight

    def setAge(self, age):
        self.age = age

    def setName(self, name):
        self.name = name.upper()

    def toString(self):
        return("Species: {}, Name: {}, Age: {}, Weight: {}"\
              .format(self.species.upper(), self.name.upper(), self.age, self.weight))
