import numpy as np
'''
    определённый интеграл от функции sin^2(x)*sin(x^2)*exp(-x^2) от 0 до 3
    по идее примерно равно 0,1667
'''

def f(x):
    return ((np.sin(x))**2) * np.sin(x**2) * np.exp(-(x**2))

def definitIntegral(func, lower, upper, numOfSegm) -> float:
    step = ((upper-lower)*1.) / numOfSegm
    x = np.arange(lower, upper, step)
    x = np.array(x+(step*1.)/2)
    x = np.array(func(x))
    z = np.array(step*x)
    return z.sum()

print(
    definitIntegral(f, 0, 3, 1_000_000)
)