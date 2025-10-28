# Apartment

class Apartment:
    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        return f"(Apartment) Rent: ${self.rent}, Distance From UCSB: {self.metersFromUCSB}m, Condition: {self.condition}"

    def __gt__(self, other):
        if self.rent > other.rent:
            return True
        elif self.rent < other.rent:
            return False
        if self.metersFromUCSB > other.metersFromUCSB:
            return True
        elif self.metersFromUCSB < other.metersFromUCSB:
            return False
        level = {"excellent":1,"average":2,"bad":3}
        if level[self.condition] > level[other.condition]:
            return True
        elif level[self.condition] < level[other.condition]:
            return False
    
        return False
    
    def __eq__(self,other):
        if self.rent == other.rent:
            if self.metersFromUCSB == other.metersFromUCSB:
                if self.condition == other.condition:
                    return True
        return False
