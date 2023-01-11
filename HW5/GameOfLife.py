from functools import partial

import numpy as np
from matplotlib import pyplot as plt


def shifter(x, a, b):
    return np.roll(np.roll(x, a, axis=0), b, axis=1)


def get_num_of_neighbours_at(mat):
    biglive = np.zeros((mat.shape[0] + 2, mat.shape[1] + 2))
    biglive[1:-1, 1:-1] = mat.astype(int)

    live_count = shifter(biglive, -1, -1) + shifter(biglive, -1, 0) + shifter(biglive, -1, 1) + shifter(biglive, 0,
                                                                                                        -1) + shifter(
        biglive,
        0,
        1) + shifter(
        biglive, 1, -1) + shifter(biglive, 1, 0) + shifter(biglive, 1, 1)
    live_count = live_count[1:-1, 1:-1]

    return live_count


def enforce_game_rule_on(src_mat, des_mat, dense_map, x, y, min, max):
    num_of_neighbours = dense_map[x, y]
    if src_mat[x, y] == 1:
        if num_of_neighbours < min or num_of_neighbours > max:
            des_mat[x, y] = 0
        else:
            des_mat[x, y] = 1
        return

    if num_of_neighbours == max:
        des_mat[x, y] = 1

def game_of_life(min_neighbours, max_neighbours, starting_dense):
    n = 256
    mat = np.random.rand(n, n)
    mat[mat > starting_dense] = 1
    mat[mat <= starting_dense] = 0

    while mat.any():
        plt.imshow(mat, cmap='gray')
        plt.show()

        new_mat = mat.copy()

        dense_map = get_num_of_neighbours_at(mat)
        for i in range(n):
            for j in range(n):
                enforce_game_rule_on(mat, new_mat, dense_map, i, j, min_neighbours, max_neighbours)
        mat = new_mat

        # dense_map = get_num_of_neighbours_at(mat)
        # new_life = (mat == 0) & (dense_map == 3)
        # end_life = (mat == 1) & ((dense_map > 3) | (dense_map < 2))
        # mat[new_life] = 1
        # mat[end_life] = 0


game_of_life(2, 3, 0.5)
