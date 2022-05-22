class DefultDict:

    def get(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            return self.func()

    def set(self, key, value):
        self.dict[key] = value

    def __init__(self, func):
        self.func = func
        self.dict = {}



def cache(fun):

    CachedDict = {}

    def func(key):
        CachedDict[key] = fun(key)
        return CachedDict[key]
    return func



def partial(func, *args, **keywords):

    def newfunc(*fargs, **fkeywords):
        newkeywords = {**keywords, **fkeywords}
        return func(*args, *fargs, **newkeywords)

    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc



def fibbonachi(count):
    a = 0
    b = 1
    print(a, end = ' ')
    for i in range(0, count):
        print(b, end = ' ')
        a, b = b, b + a

fibbonachi(20)