import numpy as np
import sounddevice as sd


# 0.1

def get_func(sec, fs, freq):
    t = np.arange(0, sec, 1 / fs)
    return np.sin(2 * np.pi * t * freq)


fs = 10000

res = get_func(5, fs, 1209) + get_func(5, fs, 697)

sd.play(res, fs)


# 0.1.1
def get_sum_funcs(sec, fs, freqs):
    return sum(map(lambda freq: get_func(sec, fs, freq), freqs))


def freq_board(index):
    a = (1209, 1336, 1477, 1633)
    b = (697, 770, 852, 941)
    return a[index % 4], b[index // 4]


def t(index, fs, sample_time):
    return get_sum_funcs(sample_time, fs, freq_board(index))


def dail(phone_number):
    temp = phone_number
    while temp != "":
        sd.play(t(int(temp[0]), 10000, 1), 10000, blocking=True)
        temp = temp[1:]


dail("0507486317")


# 0.2

def gram_schmidt_algo(mat):
    res_mat = np.zeros(mat.shape, dtype=np.float64)
    for i in range(mat.shape[1]):
        v = mat[:, i].reshape(-1, 1)
        for j in range(i):
            u = res_mat[:, j].reshape(-1, 1)
            v = v - (np.vdot(u.T, v) / np.vdot(u.T, u)) * u
        res_mat[:, i] = v.reshape((-1,))
    for i in range(res_mat.shape[1]):
        res_mat[:, i] = res_mat[:, i] / np.linalg.norm(res_mat[:, i], axis=0)
    return res_mat


print(gram_schmidt_algo(np.array([[1, 2, 3], [-1, 0, -3], [0, -2, 3]])))
