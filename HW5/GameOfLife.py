from functools import partial

import numpy as np
from matplotlib import pyplot as plt


def get_num_of_neighbours_at(mat, x, y):
    s = 0
    x_roll = 0
    size = mat.shape
    if x == 0:
        x_roll = 1
        x += 1
    elif x == size[0] - 1:
        x_roll = -1
        x -= 1

    y_roll = 0
    if y == 0:
        y_roll = 1
        y += 1
    elif y == size[1] - 1:
        y_roll = -1
        y -= 1

    mm = np.roll(mat, (x_roll, y_roll), axis=(0, 1))
    s += np.sum(mm[x - 1:x + 2, y - 1])
    s += np.sum(mm[x - 1:x + 2, y + 1])
    s += np.sum(mm[x - 1, y])
    s += np.sum(mm[x + 1, y])
    return s


def enforce_game_rule_on(src_mat, des_mat, x, y):
    num_of_neighbours = get_num_of_neighbours_at(src_mat, x, y)
    if src_mat[x, y] == 1:
        if num_of_neighbours <= 1 or num_of_neighbours >= 3:
            des_mat[x, y] = 0
        return

    if num_of_neighbours == 3:
        des_mat[x, y] = 1


def game_of_life(min_neighbours, max_neighbours, starting_dense):
    n = 256
    mat = np.zeros((n, n))
    for i in range(int(starting_dense ** 0.5)):
        for j in range(int(starting_dense ** 0.5)):
            mat[i, j] = 1

    while (True):
        new_mat = mat.copy()

        # f = np.vectorize(partial(enforce_game_rule_on, src_mat=mat, des_mat=new_mat))
        f = partial(enforce_game_rule_on, src_mat=mat, des_mat=new_mat)
        for i in range(n):
            for j in range(n):
                f(x=i, y=j)
        mat = new_mat
        plt.imshow(mat, cmap='gray')
        plt.show()


game_of_life(0, 0, 25)
# m = np.zeros((5, 5))
# x = 0
# y = 0
# m[x, y] = 1
# m[4, 4] = 1
# m[x + 1, y + 1] = 1
# print(get_num_of_neighbours_at(m, x, y))
