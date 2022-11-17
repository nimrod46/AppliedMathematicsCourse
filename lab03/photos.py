import random

import matplotlib.image as plt_img
import matplotlib.pyplot as plt
import numpy as np

# 3
img = plt_img.imread("colors.png")
src_img = img
# 4
print("type: " + str(type(img)))

# 5
print(np.shape(img))

# 6
plt.imshow(img)
plt.show()

# 7
plt.imshow(img[:, :, 0], cmap='gray')
plt.show()

plt.imshow(img[:, :, 1], cmap='gray')
plt.show()

plt.imshow(img[:, :, 2], cmap='gray')
plt.show()

plt.imshow(img[:, :, 3], cmap='gray')
plt.show()

# 8
img[:, :, 3] = np.random.uniform(0, 1, (1000, 1000))
plt.imshow(img)
plt.show()

# 9
img = img[:, :, :3]
plt.imshow(img)
plt.show()

# 10
plt.imshow(img[::-1, :, ])
plt.show()

# 11
plt.imshow(img[::, ::-1, ])
plt.show()

# 12
plt.imshow(img[:, :, 0].T, cmap='gray')
plt.show()

# 13
n = np.zeros(np.shape(img))

# 14
n[:, :, 0] = img[:, :, 0].T

# 15
n[:, :, 1] = img[:, ::-1, 1]

# 16
n[:, :, 2] = img[::-1, :, 2]

# 17
plt.imshow(n, cmap='gray')
plt.show()

# 18
plt.imshow(img[1:, :, ] - img[:-1, :, ])
plt.show()

# 19
plt.imshow(img[:, 1:, ] - img[:, :-1, ])
plt.show()

# 20
plt.imshow(img[1:, 1:, ] - img[:-1, :-1, ])
plt.show()

# 21
plt.imshow((img[:, :, 0] + img[:, :, 1] + img[:, :, 2]) / 3, cmap='gray')
plt.show()

# 22

for i in range(np.shape(src_img)[0]):
    for j in range(np.shape(src_img)[1]):
        rgb_value = src_img[i, j, 0] + src_img[i, j, 1] + src_img[i, j, 2]
        src_img[i, j, 3] = 1 if rgb_value == 0 else np.random.uniform(0, 1)

plt.imshow(src_img, cmap='gray')
plt.show()
