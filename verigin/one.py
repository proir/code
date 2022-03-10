def main():
    a = [2,"ESr",655]
    b = [1,2,5,5777]
    print(twoListsToDict(a,b))

def mergeLists(list1,list2):
    res = []

    for i in range(len(a)):
        res.append([a[i],b[i]]) 
    return res

def twoListsToDict (keylist, valList):
    res = {}
    if len(keylist) != len(valList):
        print("Списки разных длин")
        raise Exception("Всё плоха: Списки разной длины")
    for i in range(len(keylist)):
        res[keylist[i]] = valList[i]
    return res
main()