import numpy as np
from matplotlib import pyplot as plt

from HW02.funcs import normip

# א
X = np.zeros([8, 8])
X[1, 1:3] = 1
X[1, 5:7] = 1
X[3, 3:5] = 1
X[5:7, 1::5] = 1
X[6, 2:6] = 1

Y = X.copy()
for i in range(8):
    for j in range(8):
        Y[i, j] = 1 if Y[i, j] == 0 else 0

plt.imshow(Y, cmap='gray')
plt.show()


# ב
def frobenius_inner_product(A, B):
    inner_prod = (A.T @ B).trace()
    return inner_prod / (normip(A.flatten(), 2) * normip(B.flatten(), 2))


print(frobenius_inner_product(X, Y))

# ג
count = 0
while True:
    count += 1
    Xtest = np.zeros([8, 8])
    Xtest[1:7, 1:7] = np.random.randint(0, 2, (6, 6))

    if frobenius_inner_product(Xtest, X) >= 0.7:
        break
    print("access denied")
    f, axarr = plt.subplots(1, 2)
    axarr[0].imshow(Xtest, cmap='gray')
    axarr[0].set_title("test face: " + str(count))
    axarr[1].imshow(X, cmap='gray')
    axarr[1].set_title("template face")
    plt.show()
print("access permitted")
print("It took: " + str(count) + " tries!")
