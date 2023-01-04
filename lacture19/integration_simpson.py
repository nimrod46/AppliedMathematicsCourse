import numpy as np


def simpson_integration(a, b, func, n):
    x = np.linspace(a, b, n+1)
    f = func(x)
    f[1:-1:2] *= 4
    f[2:-2:2] *= 2
    h = (b - a) / n

    y = h / 3 * np.sum(f)
    return y


a = 1
b = 3
func = lambda x: 1 / x
print(simpson_integration(a,b,func, 10000))
