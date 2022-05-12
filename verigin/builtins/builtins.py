from xml.dom import NamespaceErr
import json


def f(foo, bar):
    return f"first arg: {foo} second arg: {bar}"

print(f(1,2))

a = ["aaa", "bbb", "fff", "gggg"]

b = [f"hello {i}" for i in a if len(i) > 3]
d = {i: len(i) for i in a}

def f(*a, **b):
    print(a[2])
    print(b["foo"])

f(1, 2, 3, foo="aaa", bar="bbb")

def h(foo=None, bar=None):
    print(foo)

kwargs = {"foo": 1, "bar": 2}
h(**kwargs)

a = [
    ["foo", "bar", "baz"],
    ["Alice", "Reed", "Brittany", "White"],
    [],
    ["Hello"],
]

d = {l[1] : l[0] for l in a if len(l) >= 2}

class Item:
    def __init__(self, name, cost):
        self.Name = name
        self.Cost = cost
    def __str__(self):
        return f"{self.Name}:{self.Cost} \n"


class Buscket:
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
        return f"Total Price: {self.TotalPrice}\n"

def bread(a):
    def args(what):
        print("bread")
        sandwich(what)
        print("bread")
    return args

@bread
def sandwich(what):
    print(what)

sandwich("ham")

class DB:
    def __init__(self, fileName):
        self.fileName = fileName
        self.db = {}
        
    def __enter__(self):
        with open(self.fileName) as f:
            self.db = json.load(f)

    def list(self):
        return self.db.keys()
    
    def get(self, key):
        return self.db[key]

    def set(self, key, value):
        self.db[key] = value

    def __exit__(self, *args):
        with open(self.fileName, "w") as f:
            json.dump(self.db, f)

with DB("db.json") as db:
    db.set("key","answer")
    print(db.get("key"))