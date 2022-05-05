from pkgutil import iter_modules
import json

a = [
    ["foo", "bar", "baz"],
    ["Alice", "Reed", "Brittany", "White"],
    [],
    ["Hello"],
]
d = {l[1] : l[0] for l in a if len(l) >= 2}

# print(d) - РЕАЛИЗАЦИЯ

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

def main():
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
        return f"Total_prise: {self.Total_price} \n Items: \n {' '.join([str(item) for item in self.Items])} "

# main() - РЕАЛИЗАЦИЯ
  
   

def bread(items):
    def func(what):
        print("bread")
        items(what)
        print("bread")
    return func

def vegitables(items):
    def func(what):
        print("Tomatos")
        items(what)
        print("salad")
    return func

def mayonnaise(items):
    def func(what):
        print("mayonnaise")
        items(what) 
        print("mayonnaise")
    return func

# РЕАЛИЗАЦИЯ.
# @bread
# @mayonnaise
# @vegitables
# def sandwich(what):
#     print(what)

# sandwich("ham")

class DB:


    def __init__(self, file_name):
        self.file_name = file_name
        self.db = {}
        
    def __enter__(self):
        with open(self.file_name) as f:
            self.db = json.load(f)
        return self

    def list(self):
        return self.db.keys()

    def get(self, key):

        return self.db[key]

    def set(self, key, value):
        self.db[key] = value

    def __exit__(self, *args):
        with open(self.file_name, "w") as f:
            json.dump(self.db, f)
        

with DB("db.json") as db:
    db.set("key", "value")


with DB("db.json") as db:
    print(db.get("key"))