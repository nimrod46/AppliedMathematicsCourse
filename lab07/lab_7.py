#!/usr/bin/env python3
import math

import matplotlib

matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Optional


def polar(z: complex) -> Tuple[float, float]:
    # Returns r and theta
    # Your code here:
    a = z.real
    b = z.imag
    return np.sqrt(a ** 2 + b ** 2), math.atan2(b, a)


def get_roots(z: complex, n: int) -> np.ndarray:
    # Returns an array of n complex numbers, representing the n roots of z
    roots = np.zeros((n,), dtype=np.complex64)
    ### Your code here
    zs = polar(z)
    for k in range(n):
        roots[k] = zs[0] ** (1 / n) * (np.cos((zs[1] + 2 * np.pi * k) / n) + 1j * np.sin((zs[1] + 2 * np.pi * k) / n))
    ###
    return roots


def plot_roots(z: complex, n: int):
    # Plot the n roots of the complex number z
    # Your code here
    roots = get_roots(z, n)
    real = roots.real
    imag = roots.imag
    real = np.append(real, roots[0].real)
    imag = np.append(imag, roots[0].imag)
    plt.plot(real, imag)


def run(z: complex, n: int, figure: Optional[str]):
    plt.close()
    plot_roots(z, n)
    if figure is None:
        plt.show()
    else:
        plt.savefig(figure)


if __name__ == '__main__':
    run(z=1 + 1j,
        n=2000,
        figure='fig.png')
