from functools import partial

import numpy as np
from matplotlib import pyplot as plt


def shifter(x, a, b):
    return np.roll(np.roll(x, a, axis=0), b, axis=1)


def get_num_of_neighbours_mat(mat):
    biglive = mat.astype(int)

    live_count = shifter(biglive, -1, -1) + shifter(biglive, -1, 0) + shifter(biglive, -1, 1) + shifter(biglive, 0,
                                                                                                        -1) + shifter(
        biglive,
        0,
        1) + shifter(
        biglive, 1, -1) + shifter(biglive, 1, 0) + shifter(biglive, 1, 1)

    return live_count


def enforce_game_rule_on(src_mat, des_mat, dense_map, x, y, min, max):
    num_of_neighbours = dense_map[x, y]
    if src_mat[x, y] == 1:
        if num_of_neighbours < min or num_of_neighbours > max:
            des_mat[x, y] = 0

        return

    if num_of_neighbours == max:
        des_mat[x, y] = 1

def game_of_life(min_neighbours, max_neighbours, starting_dense):
    n = 256
    mat = np.random.rand(n, n)
    for i in range(n):
        for j in range(n):
            mat[i, j] = mat[i, j] > starting_dense

    while mat.any():
        plt.imshow(mat, cmap='gray')
        plt.show()

        new_mat = mat.copy()

        dense_map = get_num_of_neighbours_mat(mat)
        for i in range(n):
            for j in range(n):
                enforce_game_rule_on(mat, new_mat, dense_map, i, j, min_neighbours, max_neighbours)
        mat = new_mat


game_of_life(2, 3, 0.5)
