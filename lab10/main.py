import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

m = np.array(range(9)).reshape((3,3))
np.roll(m, 1, axis=0)
#the second is the size of the roll
#the first is whom to roll
#the third is on the on the y axis
#it doesnt change the matrix, returns a rolled matrix
#you can also write -1 for a reverse roll
np.roll(m, (1,2), axis=(0,1))

def sq(n):
    s = 1
    for _ in range(n):
        yield s
        #i throw out the s, and i put the function on hold,
        # when i call it again the function continues from where it stopped
        if s==1:
            s = 2
        else:
            s = s**2
    return None

for i in sq(4):
    print(i)

#if i just call sq(n) i will get a generator object ,
# an object i can call again and again until it returns null, a kind of iterator

g = sq(4)
print(next(g, None))
print(next(g, None))
print(next(g, None))
print(next(g, None))
print(next(g, None))

print(list(sq(4)))

def mu(n):
    return n*5
#this function decreases the number of parameters, bacsue * is a function that gets 2 arguments
def start(a, b):
    return a*b

from functools import partial
mu = partial(start, b=5)

ma = partial(mu, a=2)
#now ma doesnt get any parameters

#lets put fibonatchi series in a table diagonally
def fib(n):
    a = 0
    b = 1
    for _ in range(n):
        yield b
        a, b = b, a + b

    return None

#matrix_d is a dictonary that has a matrix
#fv the current number of fib seires
#a plot picture thing
def plot_fib(fv, ax, matrix_d):
    matrix = matrix_d['m']

    matrix = np.roll(matrix, (fv, fv), axis=(0, 1))
    #= 1.0 means to get the color there
    matrix[0, 0:fv, 0] = 1.0
    matrix[fv, 0:fv, 1] = 1.0
    matrix[0:fv, 0, 2] = 1.0
    matrix[0:fv, fv, :] = 1.0

    ax.imshow(matrix)
    matrix_d['m'] = matrix

fig, ax = plt.subplots()
matrix_d = {'m': np.zeros((200, 200, 3), dtype = np.float32)}
partial_plot_fib = partial(plot_fib, ax = ax, matrix_d = matrix_d)
ani = FuncAnimation(fig, partial_plot_fib, frames = fib(10), repeat=False)
plt.show(block=True)

def plot_fib_roll(fv, ax, matrix_d):
    matrix = matrix_d['m']

    matrix = np.roll(matrix, (fv, fv), axis=(0, 1))
    #= 1.0 means to get the color there
    matrix[0, 0:fv, 0] = 1.0
    matrix[fv, 0:fv, 1] = 1.0
    matrix[0, 0:fv, 2] = 1.0
    matrix[0:fv, fv, :] = 1.0

    ax.imshow(matrix)
    matrix_d['m'] = matrix
