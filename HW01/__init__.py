import sys

import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def start():
    # matplotlib.use('TkAgg')

    print("------Ex1:------")

    A = np.array([[1, 1, 0], [1, -2, 1], [2, 1, 2]])
    x = np.array([[1], [2], [-2]])
    B = np.array([[1, -1, 1], [-1, 0, 1], [3, 2, 1]])
    y = np.array([2, -1, 3])
    C = np.array([[1, complex(0, -1)], [-1, complex(0, 1)], [0, complex(0, 2)]])

    print("Ax:\n" + str(A @ x))
    print()
    print("BxC: " + "Illegal!")
    print()
    print("yAB: " + str(y @ A @ B))
    print()
    print("C(C^t)x:\n" + str(C @ C.transpose() @ x))
    print()
    print("yx: " + str(y @ x))
    print()

    AB = A @ B
    print("sum1: " + str(AB.sum()))

    sum = 0
    for i in range(AB.shape[0]):
        for j in range(AB.shape[1]):
            sum += AB[i][j]

    print("sum2: " + str(sum))

    print()
    print("------Ex2:------")
    print()

    u = np.array([[complex(0, 2), 3, 5, -2, 5]]).transpose()
    v = np.array([[complex(0, 1), complex(0, -1), 2, 1, 5]]).transpose()
    w = np.array([[2, 3, complex(0, -3), -1, 3]]).transpose()

    print("<u, 2v>: " + str(inner_prod(u, 2 * v)))
    print("<u, v + 2w>: " + str(inner_prod(u, v + 2 * w)))

    print()
    print("------Ex3:------")
    print()

    fs = 44100
    Ts = 1 / fs
    x = np.arange(0, 1 - Ts, Ts)

    y1 = np.cos(2 * np.pi * 1 * x)

    y2 = np.sin(2 * np.pi * 1 * x)

    plt.plot(x, y1, 'b', x, y2, 'r')

    plt.show()

    print("<y1, y2>(1): " + str(inner_prod(np.array([y1]).transpose(),
                                           np.array([y2]).transpose())))

    print("<y1, y2>(2): " + str((y1 * y2).sum()))


def inner_prod(u, v):
    if u.shape[1] != 1 or v.shape[1] != 1:
        print("Bad arguments: input is not a column vector!", file=sys.stderr)
        return 0
    if u.shape != v.shape:
        print("Bad arguments: vector length does not match!", file=sys.stderr)
        return 0
    return np.vdot(u, v)


if __name__ == '__main__':
    start()
