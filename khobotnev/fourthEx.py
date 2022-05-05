import json


a = [
    ["foo", "bar", "baz"],
    ["Alice", "Reed", "Brittany", "White"],
    [],
    ["Hello"],
]

d = {
    l[1]: l[0] for l in a if (len(l) >= 2)
}

def main():
    # x = Student("aaa", "bbb", "ccc")
    # studentPrint(studentObj=x)
    # studentPrint("aaa", "bbb", "ccc")
    busket = Busket()
    tomato = Item("tomato", 1.55)
    banana = Item("banana", 2.12)
    vine = Item("vine", 14.90)

    busket + tomato
    busket + banana 
    busket + vine
    print(busket)
    busket - vine
    print(busket)
    pass

def studentPrint(first_name=None, second_name=None, major_subject = "Engeniring", studentObj = None):
    if(studentObj is not None):
        studentObj.print()
    elif(first_name is None and second_name is None):
        raise Exception("All's bad")
    else:
        x = Student(first_name, second_name, major_subject)
        x.print()

class Student:
    def __init__(self, first_name, second_name, major_subject):
        self.first_name = first_name
        self.second_name = second_name
        self.major_subject = major_subject
    def print(self):
        print(f"Name: {self.first_name} Surname: {self.second_name} Major: {self.major_subject}")


class Item:
    def __init__(self, name, cost):
        self.Name = name
        self.Cost = cost
    def __str__(self):
        return f"{self.Name}: {self.Cost} \n"


class Busket:
    def __init__(self):
        self.Items = []
        self.TotalPrice = 0

    def __add__(self, item):
        self.Items.append(item)
        self.TotalPrice += item.Cost
        return self

    def __sub__(self, item):
        self.Items.remove(item)
        self.TotalPrice -= item.Cost
        return self

    def __str__(self):
        return f"Total Price: {self.TotalPrice} \n{ ''.join([str(item) for item in self.Items])}"

def bread(fun):
    def bfunc(what):
        print("bread")
        fun(what)
        print("bread")
    return bfunc

def mayonnaise(fun):
    def mfunc(what):
        print("mayonnaise")
        fun(what)
    return mfunc

def vegetables(fun):
    def vfunc(what):
        print("tomatoes")
        fun(what)
        print("salad")
    return vfunc


@bread
@mayonnaise
@vegetables
def sandwich(what):
    print(what)


# main()
# print(a)
# print(d)