import numpy as np

def f(x):
    return ((np.sin(x))**2) * np.sin(x**2) * np.exp(-(x**2))  #взяла функцию в файлах у других

def Integral(func, lower, upper, numOfSegm) -> float:
    step = ((upper-lower)*1.) / numOfSegm
    x = np.arange(lower, upper, step)
    x = np.array(x+(step*1.)/2)
    x = np.array(func(x))
    z = np.array(step*x)
    return z.sum()

print(Integral(f, 0, 3, 1_000_000))

#если использовать numpy по макимуму, то можно воспльзоваться функцией numpy.trapz(y, x, dx = 1, axis = -1),
#где в определённом диапазоне найти x и y функции, представить их, как массив, и использовать эту функцию
#пример
def trapz(min = 0, max = 3):
    x = []
    y = []
    for i in range(min, max):
        x.append(i)
        y.append(f(i))
    return np.trapz(y, x)

print(trapz())