import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt


def innerProduct(x1, x2, normal=0):
    ip = sum(x1 * x2)
    if normal == 1:
        N1 = np.sqrt(sum(x1 * x1))
        N2 = np.sqrt(sum(x2 * x2))
        ip = ip / (N1 * N2)
    return ip


f0 = 1000
fs = 10000
dur = 10
tsig = 0.7
Nsig = int(fs * tsig)
Ts = 1 / fs

L = int(fs * dur)
nnsig = np.linspace(0, tsig, Nsig)
tt = np.linspace(0, dur, L)
tstart = 7
nstart = int(tstart * fs)
frame = Nsig
step = 100

xnoise = np.random.randn(L)
# plt.plot(tt[:100], xnoise[:100])
sig = np.cos(2 * np.pi * f0 * nnsig)
# plt.plot(nnsig[:100], sig[:100])
xnsig = np.copy(xnoise)
xnsig[nstart:nstart + Nsig] += 0.2 * sig
# plt.plot(tt[nstart - 10000:nstart + 10000 + Nsig], xnsig[nstart-10000:nstart + 10000 + Nsig])

iplen = int((L - frame) / step)
ip = np.zeros(iplen)
nnip = np.arange(0, iplen) * step
ttip = nnip * Ts

for j in range(iplen):
    x_test = xnsig[j * step:j * step + frame]
    ip[j] = innerProduct(x_test, sig, 1)

# plt.plot(ip)
toa = np.where(ip == max(ip))

nnsig = np.linspace(0, 1, Nsig)
mu = 0.1
xchirp = np.cos(2 * np.pi * f0 * nnsig + 2 * np.pi * mu * nnsig ** 2)
plt.plot(xchirp[:-250])

# x = np.arange(0, 1, 1 / fs)
# y = np.cos(2 * np.pi * x * f0)
# sd.play(y, f0, blocking=True)
# print("Finished")
# # plt.plot(x, y)
