#1 задание
# Создать функцию,
#которая в качестве аргумента принимает список и возвращает его в обратном порядке.
def Reeversed(a): 
    for i in reversed(a):
        print(i)

#Создать функцию
#которая принимает список слов и возвращает среднюю длину слов в списке.
def num(a):
    print(sum([len(world) for world in a]) / len(a))
#3 задание
#Создать функицию,
#которая принимает список слов и возвращает словарь, в котором заданы порядковые номера слов в списке
def matches(a):
    for i in range(0, len(a)):
        print(" " + str(i) + " : " a[i])

#4 задание 
#Создать функцию,
#которая принимает два списка и возвращает список из совпадающих элементов (порядок не важен)
def sovpadenie(a, b):
    isau = set(a)
    ifi = set(b)
    return list(isau & ifi)


#5 задание
from collections import defaultdict
def sort_1(a):
    d = defaultdict(list)
    max = 0
    out = []
    for i in a:
        d[len(i)].append(i)
        if len(i) > max:
            max = len(i)
    for j in range(1, max + 1 ):
        out.extend(d.get(j, []))
    return out

    














