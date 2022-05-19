import numpy as np

def f(x):
    return ((np.sin(x))**2) * np.sin(x**2) * np.exp(-(x**2))

def Integral(func, lower, upper, numOfSegm) -> float:
    step = ((upper-lower)*1.) / numOfSegm
    x = np.arange(lower, upper, step)
    x = np.array(x+(step*1.)/2)
    x = np.array(func(x))
    z = np.array(step*x)
    return z.sum()

print(Integral(f, 0, 3, 1_000_000))
