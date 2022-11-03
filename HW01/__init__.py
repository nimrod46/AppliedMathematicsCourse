import sys

import numpy as np


def start():
    A = np.array([[1, 1, 0], [1, -2, 1], [2, 1, 2]])
    x = np.array([[1], [2], [-2]])
    B = np.array([[1, -1, 1], [-1, 0, 1], [2, -1, 3]])
    y = np.array([[2, -1, 3]])
    C = np.array([[1, complex(0, -1)], [-1, complex(0, 1)], [0, complex(0, 2)]])
    print()
    print("Ax: " + str(A @ x))
    # print("BxC: " + B @ x @ C)
    print()
    print("BxC: " + "Illegal!")
    print()
    print("yAB: " + str(y @ A @ B))
    print()
    print("CC^tx: " + str(C @ C.transpose() @ x))
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

    u = np.array([complex(0, 2), 3, 5, -2, 5]).transpose()
    v = np.array([complex(0, 1), complex(0, -1), 2, 1, 5]).transpose()
    w = np.array([2, 3, complex(0, -3), -1, 3]).transpose()
    print("<u, 2v>: " + str(innerProd(u, 2 * v)))
    print("<u, v + 2w>: " + str(innerProd(u, v + 2 * w)))


    


def innerProd(u, v):
    if u.shape[0] != v.shape[0]:
        print("Bad argumants: input is not a column vector!", file=sys.stderr)
        return 0
    return np.inner(u, v)


if __name__ == '__main__':
    start()
