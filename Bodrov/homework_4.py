import time
class defaultdict:
    def __init__(self, lisT):
        self.dict = lisT
        if type(lisT) is  dict:
            print("словарь считан")
   
    def get(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            return 0

# D = {1:"jni", 2: "ji", 3:"nknk"}

# Dict = defaultdict(int)
# Dict.__init__(D)
# print(Dict(D, "2"))

def cache(func):
    cch = {}
    def f(arg):
        if arg in cch:
            return cch[arg]
        cch[arg] = func(arg)
        return cch[arg]
    return f

# @cache
# def slow(name):
#     time.sleep(3)
#     return "hello " + name


# print(slow("Elena"))
# print(slow("Elena"))
# print(slow("Michail"))##реализация

    


    
def partial(func, *args):
    def newfunc(*fargs):
        return func(*args, *fargs)
    newfunc.func = func
    newfunc.args = args
    return newfunc

def Fibbanachi():
    numb_1 = 1
    numb_2 = 1
    while True:
        step = numb_1
        numb_1, numb_2 = numb_2, numb_1 + numb_2
        yield step

# x = Fibbanachi()
# for _ in range(0,20):
#     print(next(x)) ##реализация
        