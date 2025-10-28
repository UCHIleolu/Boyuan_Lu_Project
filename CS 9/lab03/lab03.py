def multiply(x,y):
    if x == 0 or y == 0:
        return 0
    return x+multiply(x,y-1)

def collectMultiples(intlist, n):
    if not intlist:
        return []
    elif intlist[0]%n == 0:
        return [intlist[0]]+collectMultiples(intlist[1:],n)
    else:
        return collectMultiples(intlist[1:],n)

def countVowels(s):
    if not s:
        return 0
    elif s[0] in 'AEIOUaeiou':
        return 1 + countVowels(s[1:])
    else:
        return countVowels(s[1:])

def reverseVowels(s):
    if not s:
        return ""
    if s[0] in "aeiouAEIOU":
        return reverseVowels(s[1:]) + s[0]
    else:
        return reverseVowels(s[1:])

def removeSubString(s, sub):
    if not s:
        return ""

    if len(s) < len(sub):
        return s

    if s[:len(sub)] == sub:
        return removeSubString(s[len(sub):], sub)

    return s[0] + removeSubString(s[1:], sub)
