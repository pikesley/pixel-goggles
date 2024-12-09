import time
from random import random

from lib.colour_tools import just_an_rgb, scale_colour
from lib.context import length, pixels


def sparkle():
    """Randomly light up."""
    sleep_time = 1000

    while True:
        colour = just_an_rgb()

        for index in range(length):
            pixels[index] = scale_colour(colour, random())  # noqa: S311

        pixels.write()
        time.sleep_ms(sleep_time)
