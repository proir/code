def main():
    a = [1, 2, 3]
    b = ["One", "Two", "Three"]
    print(twoListToDict(a,b))
    c = input()
def twoListToDict(keyList, valList):
    c = {}
    for i in range(len(keyList)):
        c[keyList[i]] = valList[i]
    return c
def mergeLists(list1, list2):
    c = []
    for i in range(len(list1)):
        c.append([list[i], list2[i]])
    return c