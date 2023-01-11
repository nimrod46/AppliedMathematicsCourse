from functools import partial

import numpy as np
import scipy
from matplotlib import pyplot as plt


def darboux_integration(func, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n)
    f = func(x)
    y = h * np.sum(f[:-1])
    return y


def trapezoid_integration(func, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n)
    f = func(x)
    f[1:-1] *= 2
    y = h * np.sum(f) / 2
    return y


def simpson_integration(func, a, b, n):
    x = np.linspace(a, b, n + 1)
    f = func(x)
    f[1:-1:2] *= 4
    f[2:-2:2] *= 2
    h = (b - a) / n

    y = h / 3 * np.sum(f)
    return y


def num_integral(func, a, b, n, method='simpson'):
    """
    num_integral computes the area under the curve of a given function
    func over the interval [a,b].
    Input arguments: func - a string containing the function for which
    the area is computed.
    a, b – left and right delimiters of the section.
    n – number of sub-intervals.
    method – 'darboux', 'trapez', or 'simpson' [default].
    The function returns a scalar y – the area of f(x) under the curve
    over the interval [a,b].
    Usage: y = num_integral(func, a, b, n, method)
    Example: y=num_integral('x.^2', 0,1, 10000, 'simpson')
    """
    func_dict = {'darboux': darboux_integration, 'trapez': trapezoid_integration, 'simpson': simpson_integration}

    return func_dict[method](func, a, b, n)


def FourierEstComplex(m, N, func, xl=-np.pi, xr=np.pi, method='quad'):
    """
    FourierEstComplex computes a partial sum of Fourier series
    for a given function on the interval [a,b]. The Fourier coefficients
    cn are calculated numerically. The function returns a vector, which is
    the Fourier complex series estimate of the (sampled) function using
    the partial sum.
    Input arguments: m - partial sum order
    xl - the left delimiter of the section (of the x axis [default –pi])
    xr - the right delimiter of the section (of the x axis [default pi])
    N - number of points on the x axis.
    func - a string containing the function for which the series is
    computed.
    method - the method to integrate with ('darboux', 'trapez', 'simpson', 'quad')
    default is quad.
    The function returns the vector y - the partial sum of the Fourier
    series
    Usage: y = FourierEstComplex(m, N, func, xl, xr)
    Example: y=FourierEstComplex(150,10000,'x.^2', -1, 1)
    """
    if method != 'quad':
        integration_func = partial(num_integral, a=xl, b=xr, n=N, method=method)
    else:
        integration_func = lambda f: scipy.integrate.quad(f, a=xl, b=xr)[0]
    x_sample = np.linspace(xl, xr, N)
    sample_func = func(x_sample)
    approx_func = np.zeros(N, dtype="complex128")
    norm = 1 / (xr - xl)
    for n in range(-m, m + 1):
        c_n_re = integration_func(lambda x: np.real(func(x) * np.exp(-1 * norm * 2 * np.pi * 1j * n * x)))
        c_n_im = integration_func(lambda x: np.imag(func(x) * np.exp(-1 * norm * 2 * np.pi * 1j * n * x)))
        c_n = c_n_re + 1j * c_n_im
        c_n *= norm
        approx_func += c_n * np.exp(norm * 2 * np.pi * 1j * n * x_sample)

    fig, ax = plt.subplots(1)

    ax.plot(x_sample, approx_func, color='red')
    ax.plot(x_sample, sample_func, color='blue', linestyle='dashdot')

    plt.show()
    return approx_func


print(FourierEstComplex(150, 10000, lambda x: x ** 2, -1, 1, 'simpson'))
# f = lambda x: x * np.exp(-x)
# a = 0
# b = 2
# n = 100
#
# print(num_integral(f, a, b, n, 'simpson'))
# print(num_integral(f, a, b, n, 'trapez'))
# print(num_integral(f, a, b, n, 'darboux'))
