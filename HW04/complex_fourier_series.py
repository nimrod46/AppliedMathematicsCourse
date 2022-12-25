import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from numpy import dtype

def FourierSynthezis_complex(func, cn, N, m):
    """

    """
    x = np.linspace(-np.pi, np.pi, N)
    e = np.e
    pi = np.pi
    f = eval(func)
    plt.figure(1)
    plt.plot(x, f, 'blue')

    Sm = np.zeros(x.size, dtype='complex128')
    for n in range(-m, m):
        c_n = eval(cn)
        Sm += c_n * np.exp(1j * n * x)
        plt.figure(1)
        plt.plot(x, Sm)
        plt.grid(axis='both')
        stitle = 'Fourier seriese n = ' + str(n)
        plt.title(stitle)
        plt.figure(1)
        plt.plot(x, f, 'r')
        plt.show()
        plt.close()
    y = Sm
    return y


# f(x) = x
a0 = 0
cn = '(((-1)**n)*(e**pi-e**(-pi)))/((2*pi)*(1-1j*n))'
func = 'e**x'


cn = '(1j*(-1)**n)/(n) if n != 0 else 0'
func = 'x'
m = 100
N = 10000
FourierSynthezis_complex(func, cn, N, m)
