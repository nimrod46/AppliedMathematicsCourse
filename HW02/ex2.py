import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import time


def get_cos_array(min_bound, max_bound, sample_freq, f0):
    t = np.arange(min_bound, max_bound, sample_freq)
    x = np.cos(2 * np.pi * f0 * t)
    return x, t


def play_at_freq(freq):
    fs = 10000
    x, t = get_cos_array(0, 1, 1 / fs, freq)
    print("Playing at: " + str(freq) + " freq")
    sd.play(x, fs, blocking=True)
    plt.plot(t[:100], x[:100])
    plt.show()


def cos_play500():
    for freq in range(500, 20500, 500):
        play_at_freq(freq)


cos_play500()


def cos_play_chromatic():
    freq = 440
    while freq <= 20000:
        play_at_freq(freq)
        freq = freq * 2 ** (1 / 12)


cos_play_chromatic()
