# testFile
from Apartment import Apartment
from lab06 import *

#test Apartment
def test_getRent():
    a = Apartment(1557, 200, "bad")
    assert a.getRent() == 1557

def test_getMetersFromUCSB():
    a = Apartment(1557, 200, "bad")
    assert a.getMetersFromUCSB() == 200

def test_getCondition():
    a = Apartment(1557, 200, "bad")
    assert a.getCondition() == "bad"

def test_getApartmentDetails():
    a = Apartment(1557, 200, "bad")
    expected_output = "(Apartment) Rent: $1557, Distance From UCSB: 200m, Condition: bad"
    assert a.getApartmentDetails() == expected_output

def test_gt_operator():
    a1 = Apartment(1557, 200, "average")
    a2 = Apartment(1002, 195, "bad")
    assert (a1 > a2) == True
    assert (a2 > a1) == False

def test_eq_operator():
    a1 = Apartment(1557, 200, "bad")
    a2 = Apartment(1557, 200, "bad")
    assert (a1 == a2) == True
    a3 = Apartment(1678, 300, "average")
    assert (a1 == a3) == False

#test lab06

def test_mergesort():
    a0 = Apartment(1200, 300, "bad")
    a1 = Apartment(1000, 250, "average")
    a2 = Apartment(1000, 250, "excellent")
    a3 = Apartment(1000, 200, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    sorted_list = mergesort(apartmentList)
    expected_list = [a5, a4, a3, a2, a1, a0]
    assert sorted_list == expected_list

def test_ensureSortedAscending():
    a0 = Apartment(1200, 200, "bad")
    a1 = Apartment(1000, 215, "average")
    a2 = Apartment(1000, 215, "excellent")
    a3 = Apartment(1000, 190, "excellent")
    apartmentList = [a0, a1, a2, a3]
    sortlist = mergesort(apartmentList)

    assert ensureSortedAscending(sortlist) == True

def test_getBestApartment():
    a0 = Apartment(1200, 200, "bad")
    a1 = Apartment(1000, 215, "average")
    a2 = Apartment(1000, 215, "excellent")
    a3 = Apartment(1000, 190, "excellent")
    apartmentList = [a0, a1, a2, a3]

    expected_output = "(Apartment) Rent: $1000, Distance From UCSB: 190m, Condition: excellent"
    assert getBestApartment(apartmentList) == expected_output

def test_getWorstApartment():
    a0 = Apartment(1200, 200, "bad")
    a1 = Apartment(1000, 215, "average")
    a2 = Apartment(1000, 215, "excellent")
    a3 = Apartment(1000, 190, "excellent")
    apartmentList = [a0, a1, a2, a3]

    expected_output = "(Apartment) Rent: $1200, Distance From UCSB: 200m, Condition: bad"
    assert getWorstApartment(apartmentList) == expected_output

def test_getAffordableApartments():
    a0 = Apartment(1200, 200, "bad")
    a1 = Apartment(1000, 215, "average")
    a2 = Apartment(1000, 215, "excellent")
    a3 = Apartment(1000, 190, "excellent")
    apartmentList = [a0, a1, a2, a3]

    budget = 1100
    expected_output = "(Apartment) Rent: $1000, Distance From UCSB: 190m, Condition: excellent\n(Apartment) Rent: $1000, Distance From UCSB: 215m, Condition: excellent\n(Apartment) Rent: $1000, Distance From UCSB: 215m, Condition: average"
    assert getAffordableApartments(apartmentList, budget) == expected_output
