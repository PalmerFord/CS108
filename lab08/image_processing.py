"""CS 108 - Homework 4

This module implements image processing functions using the Python Imaging
Library (PIL) to load and display images, and NumPy to manipulate the image's
2D array of pixels.

Each pixel is represented as a list of intensity values for red, green and blue
(RGB), each value between 0 (low intensity) and 255 (high intensity).
For example:
    [0, 0, 0] represents black
    [255, 255, 255] represents white
    [255, 0, 0] represents red

@author: Palmer Ford (pjf5)
@date: fall, 2021
"""

from PIL import Image
import numpy as np
from copy import deepcopy
from guizero import App, Picture


def load_image(filename):
    """ This function loads an image from the specified file. """

    # Convert pixel values to integer format in order to
    # allow arithmetic that may overflow np's default uint8.
    return np.array(Image.open(filename), dtype='int32')


def display_image(image_array):
    """ This function displays the given image in a separate GuiZero window. """

    # Clip pixel values back to 8-bit range for display.
    image = Image.fromarray(np.uint8(np.clip(image_array, 0, 255)))

    # Show the image in a guizero window.
    app = App(width=image_array.shape[1], height=image_array.shape[0])
    Picture(app, image=image)
    # Bring the guizero window to the front
    # https://stackoverflow.com/a/36191443/69707
    root = app.tk
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    app.display()
    
def polarise_rgb_value(pc_value, average):
    """ This function takes a pixel colour value and an average and returns either 255 or 0 depending on if the pixel colour value is greater than or less than that average """
    value = 0
    if pc_value > average:
        value = 255
    return value


def change_brightness(image, delta):
    """ This function changes the brightness of the given image. """

    num_rows = len(image)
    num_columns = len(image[0])

    # Increase or decreases each RGB pixel value
    # (see the header documentation for information on RGB values).
    for row_index in range(num_rows):
        for column_index in range(num_columns):
            # Get the RGB value list for the current pixel.
            rgb = image[row_index][column_index]
            # Insert a new RGB value list with increased or decreased intensities for all
            # three colors (R, G & B).
            image[row_index][column_index] = [
                rgb[0] + delta,
                rgb[1] + delta,
                rgb[2] + delta
            ]
            
    return image

def flip_horizontal(image):
    """ This function mirrors the given image around a vertical line. """

    # This comment is necessary because you need to preserve the original so that you have somthing to base the points of the flipped image on
    image_copy = deepcopy(image)

    num_rows = len(image)
    num_columns = len(image[0])

    for row_index in range(num_rows):
        for column_index in range(num_columns):
            image[row_index][column_index] = image_copy[row_index][num_columns - column_index - 1]

    return image

def flip_vertical(image):
    """ This function mirrors the given image around a horizontal line. """

    # This comment is necessary because you need to preserve the original so that you have somthing to base the points of the flipped image on
    image_copy = deepcopy(image)

    num_rows = len(image)

    for row_index in range(num_rows):
        image[row_index] = image_copy[num_rows - row_index - 1]

    return image

def negative(image):
    """ Produces a negative image of the original. """

    num_rows = len(image)
    num_columns = len(image[0])

    # reverses each pixel value
    # (see the header documentation for information on RGB values).
    for row_index in range(num_rows):
        for column_index in range(num_columns):
            # Get the RGB value list for the current pixel.
            rgb = image[row_index][column_index]
            # Insert a new RGB value list with reversed values for all
            # three colors (R, G & B).
            image[row_index][column_index] = [
                255 - rgb[0],
                255 - rgb[1],
                255 - rgb[2]
            ]
            
    return image

def gray_scale(image):
    """ Produces a gray_scaled version of the original image. """

    num_rows = len(image)
    num_columns = len(image[0])

    # change the rgb values of each pixel to all be the average of its rgb values
    # (see the header documentation for information on RGB values).
    for row_index in range(num_rows):
        for column_index in range(num_columns):
            # Get the RGB value list for the current pixel.
            rgb = image[row_index][column_index]
            # Insert a new RGB value list with averaged values for all
            # three colors (R, G & B).
            image[row_index][column_index] = [
                (rgb[0] + rgb[1] + rgb[2]) / 3,
                (rgb[0] + rgb[1] + rgb[2]) / 3,
                (rgb[0] + rgb[1] + rgb[2]) / 3
            ]
            
    return image

def polarize(image):
    """ Produces a polarized version of the original image. """

    num_rows = len(image)
    num_columns = len(image[0])

    # Finds the averages of all R values, G values, and B values in a given image
    p_count = 0
    r_average = 0
    g_average = 0
    b_average = 0
    # (see the header documentation for information on RGB values).
    for row_index in range(num_rows):
        for column_index in range(num_columns):
            p_count += 1
            # Get the RGB value list for the current pixel.
            rgb = image[row_index][column_index]
            # Accumulates all R values, G values, and B values
            r_average += rgb[0]
            g_average += rgb[1]
            b_average += rgb[2]
    # Divides the accumulations by the total number of pixels
    r_average = r_average / p_count
    g_average = g_average / p_count
    b_average = b_average / p_count

    # Changes the rgb values of each pixel to be either 255 or 0 based on whether the value is greater or less than the average value for that color across the whole image. 
    # (see the header documentation for information on RGB values).
    for row_index in range(num_rows):
        for column_index in range(num_columns):
            # Get the RGB value list for the current pixel.
            rgb = image[row_index][column_index]
            # Insert a new RGB value list polorized values for all
            # three colors (R, G & B).
            image[row_index][column_index] = [
                polarise_rgb_value(rgb[0], r_average),
                polarise_rgb_value(rgb[1], g_average),
                polarise_rgb_value(rgb[2], b_average)
            ]
            
    return image