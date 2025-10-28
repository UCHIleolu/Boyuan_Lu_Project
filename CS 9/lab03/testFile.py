from lab03 import *

def test_multiply():
    assert multiply(0, 5) == 0
    assert multiply(5, 0) == 0
    assert multiply(7, 4) == 28
    assert multiply(10, 11) == 110
    assert multiply(90, 7) == 630

def test_collectMultiples():
    assert collectMultiples([1, 2, 3, 4, 5, 6, 7, 8], 2) == [2, 4, 6, 8]
    assert collectMultiples([10, 20, 30, 40, 50], 3) == [30]
    assert collectMultiples([5, 10, 15, 20, 25], 5) == [5, 10, 15, 20, 25]
    assert collectMultiples([3, 6, 9, 13], 3) == [3, 6, 9]
    assert collectMultiples([1, 3, 5, 8, 9, 12], 7) == []

def test_countVowels():
    assert countVowels("hello world") == 3
    assert countVowels("I love CS9") == 3
    assert countVowels("aeiou") == 5
    assert countVowels("bdfghj") == 0
    assert countVowels("Apple") == 2

def test_reverseVowels():
    assert reverseVowels("hello world") == "ooe"
    assert reverseVowels("I love CS9") == "eoI"
    assert reverseVowels("aeiou") == "uoiea"
    assert reverseVowels("bdfghj") == ""
    assert reverseVowels("Apple") == "eA"

def test_removeSubString():
    assert removeSubString("hello world", "l") == "heo word"
    assert removeSubString("hello world", "ll") == "heo world"
    assert removeSubString("hello world", "x") == "hello world"
    assert removeSubString("hello world", "hello world") == ""
    assert removeSubString("Leoleoleo", "le") == "Leooo"


