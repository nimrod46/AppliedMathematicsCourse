import numpy as np

eps = 1e-14


def qr_factorization(A):
    Q = np.zeros(A.shape, dtype=np.float64)
    R = np.zeros((A.shape[1], A.shape[1]), dtype=np.float64)
    for j in range(A.shape[1]):
        v = A[:, j].reshape(-1, 1)
        for i in range(j):
            R[i, j] = Q[:, i].reshape(-1, 1).T @ v
            v = v - R[i, j] * Q[:, i].reshape(-1, 1)
        if sum(v * v) <= eps:
            A = np.delete(A, j, axis=1)
            continue
        v = v.reshape((-1,))
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]
    return A, Q, R


a = np.array([[1, 2, 3, 2, 1], [1, 1, -1, 1, 0], [3, 4, 1, 4, 1]]).T
A, Q, R = qr_factorization(a)
print("A: " + str(A))
print("Q: " + str(Q))
print("R: " + str(R))
