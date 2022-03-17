import random

def turnAroundList(_list):
    outList = []
    for i in range(1, len(_list)+1):
        outList.append(_list[-i])
    return outList

def averageLengtOfWords(_list):
    averLen = .0
    for i in _list:
        averLen += len(i)
    return averLen/len(_list)

def dictEntryNum(_list):
    outDict = {}
    for i in range(0, len(_list)):
        if _list[i] in outDict:
            if type(outDict[_list[i]]) != list:
                a = outDict[_list[i]]
                outDict[_list[i]] = [a, i]
            else:
                outDict[_list[i]].append(i)
            continue
        outDict[_list[i]] = [i]
    return outDict

#Неуклюже очень
def listOfOverlap(_fList, _sList):
    outList = []
    for i in _fList:
        for j in _sList:
            if (i == j) and not (i in outList):
                outList.append(i)
    return outList


def listEntryDict(_list):
    outDict = {}
    for i in _list:
        if i in outDict:
            outDict[i] += 1
            continue
        outDict[i] = 1
    return outDict

"""
    Превышает лимит рекурсий. 
    Сам алгоритм с вероятностью 95% верен, т.к. это QSort из википедии 
"""
def qSortByLen(_list):
    if(len(_list)==1):
        return _list
    elif(_list == []):
        return
    p = random.randint(0, len(_list)-1)
    #p = (int)(len(_list)/2)
    tempLower, tempEquals, tempHigher = [],[],[]
    for i in _list:
        if len(_list[p]) <  len(i):
            tempHigher.append(i)
        if len(_list[p]) == len(i):
            tempHigher.append(i)
        else:
            tempLower.append(i)
    qSortByLen(tempLower)
    qSortByLen(tempHigher)
    return tempLower+tempEquals+tempHigher

def queenBeatsFigure(queenLocated, figureLocated):
    #print(queenLocated, figureLocated)
    if (queenLocated.Height == figureLocated.Height or
        ord(queenLocated.Width) == ord(figureLocated.Width) or
        ((ord(queenLocated.Width) - ord(figureLocated.Width))/(queenLocated.Height - figureLocated.Height) in [-1, 1])):
        return True
    return False

class ChessFieldSquare:
    """ 
    fields:
        Width, Height
    """
    def __init__(self, width, height):
        width.lower()
        if (width>'h' and width<'a') or (height>8 and height<1): 
            raise Exception("Таких значений не бывает")
        self.Width, self.Height = width, height
    def __str__(self) -> str:
        return f"{[self.Width, self.Height]}"
