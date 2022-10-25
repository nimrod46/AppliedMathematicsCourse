from typing import List
import numpy as np
import scipy
import matplotlib.pyplot as plt
import pandas as pd
import time


def multi_loop(vector: List[int], change: int) -> List[int]:
    for i in range(len(vector)):
        vector[i] *= change
    return vector


def measure_run_diff(vec_size: int, num_tests: int) -> float:
    ls_np = np.array(range(vec_size))
    ls_p = list(range(vec_size))
    start = time.time()
    for i in range(num_tests):
        multi_loop(ls_p, 3)
    p_time = time.time() - start
    start = time.time()
    for i in range(num_tests):
        ls_np *= 3
    np_time = time.time() - start
    return np_time - p_time


print(measure_run_diff(1000, 10000))
