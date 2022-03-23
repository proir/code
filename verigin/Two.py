from random import random


import random

def reversList(list):
    res = list
    for i in range(len(list)):
        res.append(list[-i])
    return res

def averageLen(listWithWord):
    total_length = 0
    for word in listWithWord:
        total_length += len(word)
    return total_length / len(listWithWord)

def numOfDict(list):
    res = {}

    for i in range(0, len(list)):
        if list[i] in res:
            if type(res[list[i]]) != list:
                a = res[list[i]]
                res[list[i]] = [a, i]
            else:
                res[list[i]].append(i)
            continue
        res[list[i]] = [i]
    return res

def sameWordInLists(list1, list2):
    res = []
    for i in list1:
        for j in list2:
            if (i == j) and not (i in res):
                res.append(i)
    return res

def listInDict(list):
    res = {}
    for i in list:
        if i in res:
            res[i] += 1
            continue
        res[i] = 1
    return res

def lenSort(list):
    return sorted(list1,key = len)

def queenBeatsFigure(queenLocatedNum, queenLocatedLetter, figureLocatedNum, figureLocatedLetter):
    #print(queenLocated, figureLocated)
    if (queenLocatedNum == figureLocatedNum or
        ord(queenLocatedLetter) == ord(figureLocatedLetter) or
        ((ord(queenLocatedLetter) - ord(figureLocatedLetter))/(queenLocatedNum - figureLocatedNum) in [-1, 1])):
        return True
    return False

list1 = ['123','12342','12','2131']
list2 = [1,2,3]
print(queenBeatsFigure(1,'h',8,'e'))
