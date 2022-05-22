arg  = [
        ["foo", "bar", "baz"],
        ["Alice", "Reed", "Brittany", "White"],
        [],
        ["Hello"],
]
dict = {l[1] : l[0] for l in a if len(l) >= 2}



class Student:

    def __init__(self, first_name, second_name, major_subject):
        self.first_name = first_name
        self.second_name = second_name
        self.major_subject = major_subject

    def print(self):
        print(f"Name: {self.first_name} Surname: {self.second_name} Major: {self.major_subject}")

def print(name = None, second_name = None, object = None, major_subject = "engineering"):
    if name is not None and second_name is not None:
        s = Studend(name, second_name, major_subject)
        s.print()
    elif (name is None or second_name is None) and object is not None:
        object.print()
    else:
        print("Ошибка ввода!")
        return 0



def main():
    busket = Busket()
    tomato = Item("tomato", 1.55)
    banana = Item("banana", 2.12)
    vine = Item("vine", 14.9)

    busket + tomato + banana + vine
    print(busket)
    busket - vine
    print(busket)

class Item:

    def __init__(self, name, cost):
        self.Name = name
        self.Cost = cost

    def __str__(self):
        return f"{self.Name}: {self.Cost} \n"

class Busket:

    def __init__(self):
        self.Items = []
        self.Total_price = 0

    def __add__(self, item):
        self.Items.append(item)
        self.Total_price += item.Cost
        return self

    def __sub__(self, item):
        self.Items.remove(item)
        self.Total_price -= item.Cost
        return self

    def __str__(self):
        return f"Items: \t {' '.join([str(item) for item in self.Items])} \t Total: {self.Total_price} \n"



def bread(func):
    def wrapper():
        print ("bread")
        func()
        print ("bread")
    return wrapper

def mayonnaise(func):
    def wrapper():
        print ("mayonnaise")
        func()
    return wrapper

def vegitables(func):
    def wrapper():
        print ("tomatos")
        func()
        print ("salad")
    return wrapper

@bread
@mayonnaise
@vegitables

def sandwich(what):
    print(what)

sandwich("ham")
