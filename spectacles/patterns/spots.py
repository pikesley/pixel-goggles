import time

from lib.colour_tools import just_an_rgb
from lib.context import length, pixels
from lib.orderings import tops
from lib.tools import cos_curve


def spots():
    """Spots."""
    spots = 4

    interval_divider = 5
    intervals = cos_curve(interval_divider)

    direction = "clockwise"
    outer_range = range(int(16 / spots), 0, -1)

    if "anti" in direction:
        outer_range = range(int(16 / spots))

    while True:
        colour = just_an_rgb()

        for i in outer_range:
            for j in range(length):
                pixels[j] = (0, 0, 0)

            for k in range(spots):
                index = int(k * (16 / spots)) + i
                pixels[(index + tops["right"]) % 16] = colour
                pixels[16 + (index + tops["left"]) % 16] = colour

            pixels.write()
            time.sleep(intervals.head)
            intervals.rotate()
