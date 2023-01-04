import numpy as np
import matplotlib.pyplot as plt
import time

nCols = 50
nRows = 50
aMat = np.zeros([nRows, nCols])
tolerance = 10
temp1 = 45
temp2 = 0
right = temp1
left = temp1
up = temp2
down = temp1
aMat[0, :] = up
aMat[-1, :] = down
aMat[:, 0] = left
aMat[:, -1] = right
plt.imshow(aMat, cmap='hot')
plt.colorbar()
plt.show()

aOldMat = np.copy(aMat)
diffMatSum = np.inf
iteration = 0
while diffMatSum > tolerance:
    up = aOldMat[:-2, 1:-1]
    down = aOldMat[2:, 1:-1]
    left = aOldMat[1:-1, :-2]
    right = aOldMat[1:-1, 2:]
    aNewMat = (up + down + left + right) / 4
    diffMatSum = np.sum(np.abs(aNewMat - aOldMat[1:-1, 1:-1]))
    aOldMat[1:-1, 1:-1] = aNewMat
    if iteration % 100 == 0:
        plt.imshow(aOldMat, cmap='hot')
        plt.grid(axis='both')
        plt.colorbar()
        plt.pause(0.001)
        plt.show()
    iteration += 1
print(iteration)