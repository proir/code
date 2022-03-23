
def mergeLists(list1,list2):
    res = []

    for i in range(len(list1)):
        res.append([list1[i],list2[i]]) 
    return res

def twoListsToDict (keylist, valList):
    res = {}
    if len(keylist) != len(valList):
        print("Списки разных длин")
        raise Exception("Всё плоха: Списки разной длины")
    for i in range(len(keylist)):
        res[keylist[i]] = valList[i]
    return res