
#числа Фибоначчи

def fib(n):    #у ребят там ошибка, поэтому вот код, который при подготовке к ЕГЭ ребят учат еще в школе, здесь n- это кол-во чисел, т.е. если вы хотите увидеть первые 20 чисел, то при вызове введите данное число 
    a, b = 0, 1  #первые два числа
    for i in range(n):
        yield a #yield грубо говоря ключевое слово, которое используется практииически как return, но немного иначе. Ф-ция вернет генератор.
        a, b = b, a + b #здесь мы получаем следующее число фибоначи


#Самостоятельно реализовать функцию аналогичную functools.partial
def partial(func, *args, **words):
    def newfunc(*fargs, **keywords2):
        alsowords = {**keywords2, **words} #тут, как я понял, нужно взаимодействовать так же, как и в примере с 3 объектами
        return func(**words, *keywords2)
    newfunc.func = func
    newfunc.args = args
    newfunc.args = words
    return newfunc



#Самостоятельно реализовать декоратор идентичный по функциональности с functools.cache
def cache(fun):
    CachedDict = {}
    def func(file):
        CachedDict[file] = fun(file)
        return CachedDict[file]
    return func

#а вот collections.defaultdict я не совсем понял, как это сделать, чтобы оно вообще работало.