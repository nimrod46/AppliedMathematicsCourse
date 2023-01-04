#!/usr/bin/env python3

import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import numpy as np
import scipy
import math


def rectangular_rule_integration(func, left, right, n_rects):
    width = (right - left) / n_rects
    x = np.arange(left + width / 2, right, width)
    y = func(x)
    return np.sum(y) * width


def fourier_series(ax, func, order, x_resolution):
    """
    ax - subplot to draw on
    func - Function pointer to estimate
    order - Order of the partial sum
    x_resolution - Number of samples on axis x
    
    Returns the fourier series coefficients
    """
    # Create two numpy vectors of length order, they will keep the fourier coefficients
    a_n = np.zeros(order)
    b_n = np.zeros(order)

    # Sample x and calculate f(x)
    x_sample = np.linspace(-np.pi, np.pi, x_resolution)
    sample_func = func(x_sample)

    # Fill a_0
    a_n[0] = scipy.integrate.quad(lambda x: func(x), -np.pi, np.pi)[0] / (2 * np.pi)

    # Fill a_n and b_n for 1 <= n < order
    for n in range(1, order):
        a_n[n] = scipy.integrate.quad(lambda x: func(x) * np.cos(x * n), -np.pi, np.pi)[0] / np.pi
        b_n[n] = scipy.integrate.quad(lambda x: func(x) * np.sin(x * n), -np.pi, np.pi)[0] / np.pi
    # Approximate f(x) using the coefficients
    approx_func = np.zeros(x_resolution)
    for n in range(1, order):
        approx_func += a_n[n] * np.cos(n * x_sample)
    for n in range(1, order):
        approx_func += b_n[n] * np.sin(n * x_sample)

    approx_func += a_n[0]
    # Plot fx over x and approxmiation over x. Using different linestyles. Add a legend.
    ax.plot(x_sample, approx_func, linestyle=(0, (3, 4)))
    ax.plot(x_sample, sample_func, linestyle='dashdot')

    # DO NOT call plt.show()

    # Return the two coefficient vectors
    return ...


def run(figure):
    ##############################
    ### Change here
    width = 3
    functions = ((11, lambda x: x ** 2, 'x^2'),
                 (2, np.cos, 'cos(x)'),
                 (7, lambda x: x, 'x'),
                 (11, lambda x: 3 ** x, '3^x'),
                 (11, np.exp, 'e^x'),
                 (11, lambda x: np.sin(x) * np.cos(x), 'cos(x) * sin(x)'))
    fig, ax = plt.subplots(math.ceil(len(functions) / width), width)

    for i, of in enumerate(functions):
        axi = ax[i // width, i % width]
        ###
        fourier_series(axi, of[1], of[0], 10000)
        axi.set_title(of[2])
    # Do not change
    if figure is None:
        fig.show()
    else:
        fig.savefig(figure)


if __name__ == '__main__':
    run(None)
    pass
