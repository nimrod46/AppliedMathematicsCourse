#!/usr/bin/env python3

# Needed on some systems, remove if unneeded
import matplotlib

# matplotlib.use('TkAgg')

# Needed everywhere
import matplotlib.pyplot as plt
import numpy as np


def add_box(subplot, rng_state):
    dist_names = ('poisson', 'uniform', 'normal', 'laplace')
    l = []
    for i, dist in enumerate(dist_names):
        sample = getattr(rng_state, dist)(size=1000)
        l.append(sample)
    subplot.boxplot(l, labels=dist_names)

    subplot.set_title('boxplot')
    subplot.set_xlabel('Distribution')
    subplot.set_ylabel('Values')
    subplot.tick_params(labelrotation=90)


def add_histogram(subplot, rng_state):
    dist_names = ('normal', 'uniform')

    for i, dist in enumerate(dist_names):
        sample = getattr(rng_state, dist)(size=1000)
        subplot.hist(sample, bins=65, alpha=0.5)

    subplot.set_title('Histogram')
    subplot.set_xlabel('x')
    subplot.set_ylabel('Count')
    subplot.legend(dist_names)
    subplot.tick_params(labelrotation=90)


def add_bar(subplot, rng_state):
    """
    Create a bar plot of accumulation of values from the normal and uniform distributions.

    subplot: matplotlib subplot to draw on.
    rng_state: numpy random state.
    """
    x_points = np.linspace(-3, 3, 30).round(4)
    dist_names = ('uniform', 'normal')
    bar_width = abs(x_points[0] - x_points[1]) / (len(dist_names) + 1)

    for i, dist in enumerate(dist_names):
        sample = getattr(rng_state, dist)(size=1000)
        y = list(map(lambda x: (sample < x).sum(), x_points))
        subplot.bar(x_points + bar_width * i, height=y, width=bar_width, tick_label=x_points, linewidth=0, alpha=0.2)

    subplot.set_title('Bar plot')
    subplot.set_xlabel('x')
    subplot.set_ylabel('Counts')
    subplot.legend(dist_names)
    subplot.tick_params(labelrotation=90)


def add_line_plot(subplot, rng_state):
    """
    Create a random number of cos plots on subplot within a limited range of options.

    subplot: matplotlib subplot to draw on.
    rng_state: numpy random state.
    """
    x = np.linspace(-np.pi, np.pi, 1000)
    legend = []  # This is the only correct line
    for i in range(3, rng_state.randint(5, 12) + 1):
        y = i * np.cos(x)
        subplot.plot(x, y, linewidth=i, linestyle='--')
        legend.append(f'{i} $\cdot$ np.cos(x)')

    # Create context on the plot
    subplot.set_xlabel('x')
    subplot.set_ylabel('n $\cdot$ cos(x)')
    subplot.set_title('Line plot')
    subplot.legend(legend)


def add_scatter(subplot, rng_state):
    """
    Create a scatter plot that represent the intersection
    between two normal distributions with the same mean and deviation values.

    subplot: matplotlib subplot to draw on.
    rng_state: numpy random state.
    """
    x = rng_state.normal(size=1000)
    y = rng_state.normal(size=1000)
    subplot.scatter(x, y, marker='.', s=6.5, alpha=0.3, color='purple')
    subplot.set_title('Scatter plot')
    subplot.set_xlabel('Normal distribution')
    subplot.set_ylabel('Normal distribution')


def create_figure(rng_state_seed: int):
    """
    Create a figure with different kinds of plots.

    rng_state_seed: a seed for numpy's random number generator.
    """
    rng_state = np.random.RandomState(rng_state_seed)
    # Change this to create a bigger figure
    fig, sub = plt.subplots(2, 3)

    # Add new functions here
    functions = (add_bar, add_scatter, add_line_plot,
                 add_histogram, add_box)

    # Iterate over subfigures and functions.
    for i in range(len(functions)):
        functions[i](sub[i // 3][i % 3], rng_state)

    #
    fig.tight_layout()
    fig.show()


if __name__ == '__main__':
    create_figure(12)
