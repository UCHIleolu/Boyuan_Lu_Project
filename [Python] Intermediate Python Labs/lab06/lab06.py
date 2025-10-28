# lab06
from Apartment import Apartment

def mergesort(apartmentList):
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2

        lefthalf = apartmentList[:mid]
        righthalf = apartmentList[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i = j = k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j] or lefthalf[i] == righthalf[j]:
                apartmentList[k] = lefthalf[i]
                i += 1
            else:
                apartmentList[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            apartmentList[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            apartmentList[k] = righthalf[j]
            j += 1
            k += 1
    
    return apartmentList

def ensureSortedAscending(apartmentList):
    for i in range(1, len(apartmentList)):
        if apartmentList[i] < apartmentList[i-1]:
            return False
    return True

def getBestApartment(apartmentList):
    sortlist = mergesort(apartmentList)
    Bapartment = sortlist[0]
    return Bapartment.getApartmentDetails()

def getWorstApartment(apartmentList):
    sortlist = mergesort(apartmentList)
    Wapartment = sortlist[-1]
    return Wapartment.getApartmentDetails()

def getAffordableApartments(apartmentList, budget):
    Aapartments = []
    sortlist = mergesort(apartmentList)
    
    for i in sortlist:
        if i.getRent() < budget or i.getRent() == budget:
            Aapartments.append(i.getApartmentDetails())
    
    return '\n'.join(Aapartments)
