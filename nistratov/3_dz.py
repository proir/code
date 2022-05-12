# 1 задание


m = [
    ["foo", "bar", "baz"],
    ["Alice", "Reed", "Brittany", "White"]
    [],
    ["Hello"],
]
k = {i[1] : i[0] for i in m if len(i) >= 2}



# 2 задание


class Studend:
    def __init__(self, first_name, second_name, major_subject):
        self.first_name = first_name
        self.second_name = second_name
        self.major_subject = major_subject
    def print(self):
        print(f"Name: {self.first_name} Surname: {self.second_name} Major: {self.major_subject}")

def printself(name = None, second_name = None,obj = None, major_subject = "cooker"):
    if name is not None and second_name is not None:
        s = Studend(name, second_name, major_subject)
        s.print()
    elif (name is not None or second_name is None) and obj is not None:
        obj.print()
    else:
        raise Exception()



# 3 задание

def main():
    busket = Busket()
    tomato = Item("tomato", 1.55)
    banana = Item("banana", 2.12)
    vine = Item("vine", 14.98)

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
        return f"TotalPrice: {self.TotalPrice} \n{ ''.join([str(item) for item in self.Items])}"



# 4 задание


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
def sandwich(what="ham"):
    print(what)
    
sandwich()


