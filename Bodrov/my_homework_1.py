from re import X

def reversList(list):
    l = []
    b=len(list)
    for i in range(b):
        l.append(list[b-i-1])
    return l
  

#-----------------------------------

def Sred(Spisok):
    sum = 0 
    b = len(Spisok)
    for n in range(b):
        sum = sum + len(Spisok[n])

    return (sum/b)


#------------------------------------------------

def ToDict(list):
    res = {}

    for i in range(0, len(list)):
        if list[i] in res:
            if type(res[list[i]]) != list:
                a = res[list[i]]
                res[list[i]] = [a, i]
            else:
                res[list[i]].append(i)
            continue
        res[list[i]] = i
    return res
#------------------------------------------------

def Sovpad(arg1, arg2):
    A=set(arg1)
    B=set(arg2)
    C = []
    C= A & B
    return C

#------------------------------------------------


def Chastota(arg):
    C = {}
    b=len(arg)
    for i in range(b):
        N=0
        for n in range(b):
            if arg[i]==arg[n]:
                N=N+1
                continue
            if n==b-1:
                C[i] = N
    return C


#--------------------------------------------

def sort(arg):
    C = []
    d=len(arg)
    for j in range(d):
        min=100
        for i in range(d):
            if len(arg[i]) < min:
                min = len(arg[i])
                n=i
        C.append(arg[n])
        del arg[n]
        d=d-1
    return C
#-----------------------------------------------------






