import time
from random import random

from lib.colour_tools import rgb_from_hue, scale_colour
from lib.context import hue_source, length, pixels


def sparkle():
    """Randomly light up."""
    sleep_time = 1000

    while True:
        colour = rgb_from_hue(hue_source.hue())["bytes"]

        for index in range(length):
            pixels[index] = scale_colour(colour, random())  # noqa: S311

        pixels.write()
        time.sleep_ms(sleep_time)
