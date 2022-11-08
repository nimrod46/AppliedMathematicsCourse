import numpy as np

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
