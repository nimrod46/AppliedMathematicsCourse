import numpy as np
from matplotlib import pyplot as plt


def draw_figure(r):
    x = np.linspace(0, 1, 10000)
    zs = r * (np.cos(2 * np.pi * x) + 1j * np.sin(2 * np.pi * x))
    fig, ax = plt.subplots()
    ax.plot(x, zs.imag)
    ax.plot(x, zs.real)
    ax.legend(['image', 'real'])
    ax.set_title('cis(theta)')
    fig.show()

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(zs, np.ones(zs.shape) * r)
    fig.show()


draw_figure(1)
