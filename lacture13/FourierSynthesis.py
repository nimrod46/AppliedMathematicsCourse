import numpy as np
import matplotlib.pyplot as plt
import time


def FourierSynthesis(a0, an, bn, func, m, N):
    """

    """
    x = np.linspace(-np.pi, np.pi, N)
    f = eval(func)
    plt.figure(1)
    plt.plot(x, f, 'blue')
    y = np.zeros(x.size)
    eps = 1e-14

    Sm = np.zeros(x.size) + (a0 / 2)
    for n in range(1, m):
        a_n = eval(an)
        b_n = eval(bn)
        Sm += a_n * np.cos(n * x) + b_n * np.sin(n * x)
        plt.figure(1)
        plt.pause(1)
        plt.plot(x, Sm)
        plt.grid(axis='both')
        stitle = 'Fourier seriese n = ' + str(n)
        plt.title(stitle)
        plt.figure(1)
        plt.plot(x, f, 'r')
        plt.show()
    y = Sm
    return y


# f(x) = x
a0 = 0
an = '0'
bn = '2*(-1)**(n+1)/n'
func = 'x'
m = 50
N = 10000
y = FourierSynthesis(a0, an, bn, func, m, N)
