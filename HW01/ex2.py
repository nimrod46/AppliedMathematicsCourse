import sys

import numpy as np


def inner_prod(u, v):
    if u.shape[1] != 1 or v.shape[1] != 1:
        raise ValueError("Bad arguments: input is not a column vector!")
    if u.shape != v.shape:
        raise ValueError("Bad arguments: vector length does not match!")
    return np.vdot(v, u)  # Vdot uses complex conjugate on the first arg, so we reverse the input


u = np.array([[complex(0, 2), 3, 5, -2, 5]]).transpose()
v = np.array([[complex(0, 1), complex(0, -1), 2, 1, 5]]).transpose()
w = np.array([[2, 3, complex(0, -3), -1, 3]]).transpose()

print("<u, 2v>: " + str(inner_prod(u, 2 * v)))
print("<u, v + 2w>: " + str(inner_prod(u, v + 2 * w)))
