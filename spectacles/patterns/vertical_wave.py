import time

from lib.colour_tools import just_an_rgb, scale_colour
from lib.context import pixels
from lib.orderings import get_pairs
from lib.tools import colour_pair, get_intervals, inverse_square_tail


def vertical_wave():
    """Waves of colour."""
    sleep_multiplier = 100

    left = get_pairs("left", "wsw")
    right = get_pairs("right", "ese")

    values = inverse_square_tail(len(left) * 3)
    intervals = get_intervals(sleep_multiplier)

    while True:
        colour = just_an_rgb()
        for index, value in enumerate(values):
            i = index % 9
            colour_pair(pixels, left[i] + right[i], scale_colour(colour, value))

        pixels.write()

        values.rotate()
        intervals.rotate(direction="r")
        time.sleep_ms(intervals.head)
