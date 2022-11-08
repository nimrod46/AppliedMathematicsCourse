import numpy as np
import matplotlib.pyplot as plt

fs = 44100
Ts = 1 / fs
x = np.arange(0, 1 - Ts, Ts)

y1 = np.cos(2 * np.pi * 1 * x)

y2 = np.sin(2 * np.pi * 1 * x)

plt.plot(x, y1, 'b', x, y2, 'r')

plt.show()

print("<y1, y2>(1): " + str(np.vdot(np.array([y1]), np.array([y2]))))

print("<y1, y2>(2): " + str((y1 * y2).sum()))
