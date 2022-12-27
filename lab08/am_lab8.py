#!/usr/bin/env python3


import matplotlib

# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import numpy as np
from pathlib import Path


def load_table(data: Path):
    f = data.open()
    results = {}
    ### Complete this function
    for line in f.read().split('\n')[1:-1]:
        words = line.split("\t")
        results[words[0]] = np.array(words[1:], dtype=np.float64)
    ###
    return results


def lp(x, y, p):
    return np.sum(np.abs(x - y) ** p) ** (1 / p)


def l6(x, y):
    return lp(x, y, 6)


def cosine(x, y):
    return np.sum(x * y) / ((np.sum(x ** 2) ** 0.5) * (np.sum(y ** 2)) ** 0.5)


def cosine_similarity(x, y):
    return 1 - cosine(x, y)


def weighted_jaccard_similarity(x, y):
    return np.sum(np.min([x, y], axis=0)) / np.sum(np.max([x, y], axis=0))


def weighted_jaccard_distance(x, y):
    return 1 - weighted_jaccard_similarity(x, y)


def samples2distances_table(samples):
    results = {}
    ### Complete this function
    # you may create a tuple of pairs, where each pair is a name of a function (as a string)
    # and the function pointer, then loop over the tuple and fill a dictionary.
    funcs = (("l6", l6), ("cosine", cosine_similarity), ("WJD", weighted_jaccard_distance))
    for name_and_func in funcs:
        n = len(samples)
        a = np.zeros((n, n))
        vectors = list(samples.values())
        for i in range(n):
            for j in range(n):
                a[i, j] = name_and_func[1](vectors[i], vectors[j])
        results[name_and_func[0]] = a
    return results


def plot_distances(results, labels, figure):
    fig, ax = plt.subplots(1, len(results))
    ### Complete this function
    for i, (k, v) in enumerate(results.items()):
        ax[i].set_title(k)
        ax[i].imshow(v, cmap='gray')
        ax[i].set_xticks(range(len(labels)), labels, rotation=90)
        ax[i].set_yticks(range(len(labels)), labels, rotation=90)
    ###
    if figure is None:
        fig.show()
    else:
        fig.savefig(figure)


def run(data: Path, figure):
    data_table = load_table(data)
    print(data_table)
    distances = samples2distances_table(data_table)
    print(distances)
    plot_distances(distances, list(data_table.keys()), figure)


if __name__ == '__main__':
    run(Path('data.tsv'),  # Replace ... with the path to the datafile
        None)
