import time

from lib.colour_tools import just_an_rgb, scale_colour
from lib.context import pixels
from lib.orderings import get_pairs
from lib.tools import colour_pair, get_intervals, inverse_square_tail


def wave():
    """Waves of colour."""
    sleep_multiplier = 50
    sequence = get_pairs("left", "w") + get_pairs("right", "w")
    values = inverse_square_tail(len(sequence))
    intervals = get_intervals(sleep_multiplier)

    while True:
        colour = just_an_rgb()
        for index, value in enumerate(values):
            colour_pair(pixels, sequence[index], scale_colour(colour, value))

            pixels.write()

        values.rotate()
        intervals.rotate(direction="r")
        time.sleep_ms(intervals.head)
