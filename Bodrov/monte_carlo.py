import numpy as np
import math
import random

def func(arg):
    return sin(arg)*sin(arg)*sin(arg*arg)*exp(-arg*arg)


def monte():
    ng = np.random.default_rng(12345)
    N = 0
    for i in range(1,100000):
        X = rng.random()
        Y = rng.random()
        if Y <= func(X):
            N = N + 1
    return N/100000
    


        
