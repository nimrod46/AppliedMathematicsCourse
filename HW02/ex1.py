import numpy as np

from HW02.funcs import normip

v = np.array([1, complex(0, 2), -3, 1, 7])
print("v norm: " + str(normip(v, 2)) + "\n")

v = np.array([1, 5, complex(0, 3), complex(-1, 1), 2])
v_norm = normip(v, 2)
print("normalized v:\n" + str(v / v_norm) + "\n")

u = np.array([2, 1, complex(0, -2), -3, 8])
v = np.array([6, 7,  complex(0, 1),  complex(0, 2), 7])

print("u and v distance: " + str(normip(u - v, 2)))

