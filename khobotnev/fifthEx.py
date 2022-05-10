class DefaultDict:
    def __init__(self, func):
        self.func = func
        self.dict = {}
    
    def get(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            return self.func()

    def set(self, key, val):
        self.dict[key] = val
        pass


def CACHE(fun):
    CachedDict = {}
    def func(*args):
        if CachedDict.get(args)==None:
            CachedDict[args] = fun(*args)
        return CachedDict[args]
    return func

def partial(func, *args):
    def newfunc(*fargs):
        return func(*args, *fargs)
    newfunc.func = func
    newfunc.args = args
    return newfunc


# def partial(func, /, *args, **keywords):
#     def newfunc(*fargs, **fkeywords):
#         newkeywords = {**keywords, **fkeywords}
#         return func(*args, *fargs, **newkeywords)
#     newfunc.func = func
#     newfunc.args = args
#     newfunc.keywords = keywords
#     return newfunc

def Fibb():
    fst, snd = 1, 1
    while True:
        tmp = fst
        fst, snd = snd, fst+snd
        yield tmp