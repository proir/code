class DefaultDict:
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

tmp = DefaultDict(int)
print(tmp.get("key"))


def Fibb():
    fst, snd =0, 1
    while True:
        tmp = fst
        fst, snd = snd, fst + snd
        yield fst

x = Fibb()
# for _ in x:
for _ in range(0,20):
    print(next(x))