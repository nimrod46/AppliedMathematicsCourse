#!/usr/bin/env python3

import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import matplotlib.image as pim

from functools import partial
from matplotlib.animation import FuncAnimation
import numpy as np


def load_circles(image_path, rng_state):
    """
    Do not change this function
    
    Loads a given image, adds noise and move the view point on the torus.
    
    image_path - Path to the picture with the circle
    rng_state - Instance of np.random.RandomState
    
    Returns the picture with random rotation and noise.
    """
    img = pim.imread(image_path)
    img[::2, ::2] += rng_state.uniform(size=img.shape)[::2, ::2]
    shift_y = rng_state.randint(0, img.shape[0])
    shift_x = rng_state.randint(0, img.shape[1])
    print(f'Shift: (y, x) = ({shift_y}, {shift_x})')
    return np.roll(img, (shift_y, shift_x), axis=(0, 1))


def subimage_iterator(img, width, height, ax, step_size, callback):
    """
    Given an image and the width/height of a reference image on a torus.
    Yields all sub-images of size height*width with step_size jumps between them.
    When a sub-image is extracted, a green rectangular is drawn around the area it was extracted along with the original image.
    
    img - source image to extract the rectangular from
    width - width of rectangular to extract
    height - height of rectangular to extract
    ax - matplotlib AxesSubplot to draw the image and the extracted rectangular from.
    step_size - step size when moving the rectangular
    callback - a function that takes and returns no parameters to be called after the last yield.
    
    
    Yields a sub area of the image, a rectangular of the given dimensions and the y,x of its upper left corner.
    subimage, y, x
    
    Returns None
    """
    green_rect = np.zeros((img.shape[0], img.shape[1], 4))

    green_rect[0, 0:width, 1] = 1
    green_rect[0 + height, 0:width, 1] = 1

    green_rect[0:height, 0, 1] = 1
    green_rect[0:height, width + 0, 1] = 1

    ### Your code goes here
    for h in range(0, img.shape[1], step_size):
        for w in range(0, img.shape[0], step_size):
            ax.clear()
            ax.imshow(img + np.roll(green_rect, (h, w), (0, 1)))
            subimage = np.roll(img, (-h, -w), (0, 1))[:height, :width, :]
            yield subimage, h, w

    ###

    callback()
    return None


def cosine(x, y):
    """
    Returns cosine similarity of x and y.
    <x, y> / (||x||_2 * ||y||_2)
    """
    ### Your code goes here
    return (np.sum(x * y)) / ((np.sum(x * x) ** 0.5) * (np.sum(y * y) ** 0.5))
    ###


def similarity_tester(sample, reference_image, results, ax, nth=4):
    """
    Do not change this function
    
    Find the highest cosine similarity and where it is located.
    
    sample - the output yielded by subimage_iterator
    reference_image - a reference we look for in the subimage contained within the sample tuple
    results - dictionary to put the function output in. Contains the following 3 keys that should be updated by the function:
        1. similarity: cosine similarity, higher is better.
        2. x: x value of the highest cosine similarity value.
        3. y: y value of the highest cosine similarity value.
    ax - matplotlib AxesSubplot thath already contains the image and the extracted rectangular from. Just add a title with similarity, y and x.
    
    Returns nothing
    """
    img_slice, y, x = sample
    similarity = cosine(reference_image, img_slice)
    if similarity > results['similarity']:
        results['similarity'] = similarity
        results['x'] = x
        results['y'] = y

    ax.set_title(f'Cosine Similarity = {round(similarity, nth)} at ({y}, {x})')


def highlight_circle(results, img, height, width, figure, ax, fig, nth=4):
    """
    Draws the noisy image and places a green rectangular where the highest cosine similarity value was found.
    Use round to the Nth digit when creating the title round(f, Nth).
    
    results - a dictionary that contains the following 3 keys:
        1. similarity: highest found cosine similarity.
        2. x: x value of the highest cosine similarity value.
        3. y: y value of the highest cosine similarity value.
    img - the full image with the circle
    height - height of the reference image
    width - width of the reference image
    figure - either a name of a figure to save or None to show the figure
    ax - matplotlib AxesSubplot to draw on
    fig - the figure ax belongs to
    nth - digit to round to
    
    Returns nothing
    """

    ### Your code goes here

    green_rect = np.zeros((img.shape[0], img.shape[1], 4))

    green_rect[0, 0:width, 1] = 1
    green_rect[0 + height, 0:width, 1] = 1

    green_rect[0:height, 0, 1] = 1
    green_rect[0:height, width + 0, 1] = 1

    ax.imshow(img + np.roll(green_rect, (results['y'], results['x']), (0, 1)))

    ax.set_title(f'Cosine Similarity = {round(results["similarity"], 4)} at ({results["x"]}, {results["y"]})')

    ###

    if figure is None:
        fig.show()
    else:
        fig.savefig(figure)


def animation_callback(results, noisy_image, reference_image, figure, ax, fig):
    """
    Do not change this function
    
    Prints the results from the search for the reference image on the full image and calls highlight_circle to draw the results.
    
    results - a dictionary that contains the following 3 keys:
        1. similarity: highest found cosine similarity.
        2. x: x value of the highest cosine similarity value.
        3. y: y value of the highest cosine similarity value.
    noisy_image - the full image with the circle
    reference_image - a clean image of the circle we look for
    figure - either a name of a figure to save or None to show the figure
    ax - matplotlib AxesSubplot to draw on
    fig - the figure ax belongs to
    
    Returns nothing
    """
    print(results)
    highlight_circle(results, noisy_image, reference_image.shape[0], reference_image.shape[1], figure, ax, fig)


def run(figure, step_size, interval, noisy_image_path, reference_image_path, seed):
    """
    Do not change this function
    
    Search for a given reference image on a noicy image drawn on a torus using cosine similarity.
    Animate the whole process. Draw the final results.
    
    figure - either a name of a picture to save the final results as or None for them to be shown directly
    step_size - step size when moving the search area on the noisy image
    interval - animation advancement intervals in milliseconds
    noisy_image_path - path to the full image on your computer
    reference_image_path - path to the reference image on your computer
    seed - seed for the random numbers generator
    
    Returns the animation object
    """

    # Initialize the random numbers generator
    rng_state = np.random.RandomState(seed)

    # Load images
    noisy_image = load_circles(noisy_image_path, rng_state)
    reference_image = plt.imread(reference_image_path)

    # -1 can never happen, so it is a safe default
    results = {'similarity': -1, 'x': -1, 'y': -1}

    fig, ax = plt.subplots()

    # create the parital functions for FuncAnimation
    partial_similarity_tester = partial(similarity_tester, reference_image=reference_image, results=results, ax=ax)
    callback = partial(animation_callback, results, noisy_image, reference_image, figure, ax, fig)

    # Run everything.
    ani = FuncAnimation(fig,
                        partial_similarity_tester,
                        frames=subimage_iterator(noisy_image, reference_image.shape[1], reference_image.shape[0], ax,
                                                 step_size, callback),
                        repeat=False,
                        interval=interval)

    plt.show(block=True)

    return ani


if __name__ == '__main__':
    ani = run(figure='res.png',
              step_size=20,
              interval=20,
              noisy_image_path='full_circle.png',
              reference_image_path='just_circle.png',
              seed=1)
