import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import time


def get_cos_array(min, max, f0):
    fs = 10000
    Ts = 1 / fs
    t = np.arange(min, max, Ts)
    x = np.cos(2 * np.pi * f0 * t)
    return x
    # sd.play(x, fs)
    # plt.plot(t, x)
    # plt.grid(axis='both')
    # stitle = 'cosine function with freq = ' + str(f0)
    # plt.title(stitle)
    # plt.show()
    # time.sleep(1)


def cos_play500():
    for i in range(500, 20000, 500):
        fs = 10000
        x = get_cos_array(0, 1, i)
        sd.play(x, fs, blocking=True)
        plt.plot(x)
        plt.show()


# cos_play500()


def cos_play_kromi():
    freq = 440
    while freq < 20000:
        fs = 10000
        x = get_cos_array(0, 1, freq)
        sd.play(x, fs, blocking=True)
        freq = freq * 2 ** (1 / 12)


cos_play_kromi()
