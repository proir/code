from logging import exception
import re


def twoListsToDict(keyLest, valList):
    c = {}
    if len(keyLest) != len(valList):
        raise exception("Все плохо: Списки разных длин")
    for i in range(len(keyLest)):
        c[keyLest[i]] = valList[i]
    return c

def mergeLists(list1, list2):
    c = []
    for i in range( len(list1) ):
        c.append([list1[i], list2[i]])
    return c