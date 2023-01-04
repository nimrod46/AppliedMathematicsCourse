import numpy as np
import matplotlib.pyplot as plt


def rect(func, a, b, n):
    """

    """
    h = (b - a) / n
    x = np.linspace(a, b, n)
    f = eval(func)
    y = h * np.sum(f[:-1])
    return y


y = rect("x**2", 0, 1, 10 ** 6)
print(y)
