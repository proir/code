def twoListsToDict(keyList, valList):
    c = {}
    if len(keyList) != len(valList):
        raise Exception("Всё плохо: Списки разных длин")
    for i in range(len(keyList)):
        c[keyList[i]] = valList[i]
    return c


def mergeLists(list1, list2):
    c=[]
    for i in range( len(list1) ):
        c.append([list1[i], list2[i]])
    return c