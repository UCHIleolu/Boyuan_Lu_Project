#AnimalShelter
from Animal import Animal

class AnimalShelter:
    def __init__(self):
        self.animalshelter={}

    def addAnimal(self, animal):
        if self.animalshelter.get(animal.species) == None:
            self.animalshelter[animal.species] = [animal]
        else:
            self.animalshelter[animal.species].append(animal)

    def removeAnimal(self, animal):
        if self.animalshelter.get(animal.species) != None:
            self.animalshelter[animal.species].remove(animal)

    def removeSpecies(self, species):
        species = species.upper()
        if self.animalshelter.get(species) != None:
            del self.animalshelter[species]

    def getAnimalsBySpecies(self, species):
        species = species.upper()
        ABS = ""
        if self.animalshelter.get(species) != None:
            for i in self.animalshelter[species]:
                ABS += i.toString()
                ABS += '\n'
            ABS = ABS[:-1]
        return ABS

    def doesAnimalExist(self, animal):
        if self.animalshelter.get(animal.species) != None:
            for i in self.animalshelter[animal.species]:
                if i.name == animal.name and i.age == animal.age and\
                   i. weight == animal.weight:
                    return True
        return False
