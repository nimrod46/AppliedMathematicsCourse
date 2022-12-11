import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt


# a
def get_chirp(f0, u, fs, dur):
    tt = np.linspace(0, dur, int(fs * dur))
    sig = np.cos(2 * np.pi * f0 * tt + 2 * np.pi * u * tt ** 2)
    return sig, tt


# b
f0 = 1000
u = 550
fs = 44100
dur = 15
sig_dur = 0.7
sig, tt = get_chirp(f0, u, fs, sig_dur)
fig, axs = plt.subplots(2)
axs[0].plot(tt[:200], sig[:200])
axs[1].plot(tt[-200:], sig[-200:])
fig.show()
# sd.play(sig, fs)

# c
n_noise = int(fs * dur)
x_noise = np.random.randn(n_noise)
n_start = int(9 * fs)
n_sig = int(fs * sig_dur)
x_noise[n_start:n_start + n_sig] += sig


# d
def find_chirp(x_noise, sig, fs, dur, sig_dur):
    def inner_product(x1, x2, normal=0):
        ip = sum(x1 * x2)
        if normal == 1:
            N1 = np.sqrt(sum(x1 * x1))
            N2 = np.sqrt(sum(x2 * x2))
            ip = ip / (N1 * N2)
        return ip

    step = 100
    noise_len = int(fs * dur)
    sig_len = int(fs * sig_dur)
    ip_len = int((noise_len - sig_len) / step)
    ip = np.zeros(ip_len)
    for j in range(ip_len):
        x_test = x_noise[j * step:j * step + sig_len]
        ip[j] = inner_product(x_test, sig, 1)
    plt.plot(ip)
    plt.show()
    toa_index = ip.argmax()
    return (toa_index * (dur - sig_dur) / ip_len), toa_index


# d
toa, sample_index = find_chirp(x_noise, sig, fs, dur, sig_dur)
print("Time of arrival: " + str(toa))
print("Sample index: " + str(sample_index))

# e
chirp = np.load('chirp.npy')
xnsig = np.load('xnsig.npy')
dur = 35
sig_dur = 0.7
toa, sample_index = find_chirp(xnsig, chirp, fs, dur, sig_dur)
print("Time of arrival: " + str(toa))
print("Sample index: " + str(sample_index))
