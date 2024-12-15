import time
from math import ceil, floor
from random import randint

from lib.colour_tools import just_an_rgb
from lib.context import length, pixels
from lib.orderings import random_rotation, tops
from lib.tools import cos_curve


def spots():
    """Spots."""
    spots = randint(2, 5)  # noqa: S311

    interval_divider = 5
    intervals = cos_curve(interval_divider)

    direction = random_rotation()
    outer_range = range(int(16 / spots), 0, -1)

    if "anti" in direction:
        outer_range = range(int(16 / spots))

    while True:
        colour = just_an_rgb()

        for i in outer_range:
            for j in range(length):
                pixels[j] = (0, 0, 0)

            for k in range(spots):
                pixels[(get_rounding(k, spots, i) + tops["right"]) % 16] = colour
                pixels[16 + (get_rounding(k, spots, i) + tops["left"]) % 16] = colour

            pixels.write()
            time.sleep(intervals.head)
            intervals.rotate()


def get_rounding(k, spots, i):
    """`floor` or `ceil`."""
    rounding_method = floor if randint(0, 1) == 1 else ceil  # noqa: S311

    return rounding_method(k * (16 / spots)) + i
