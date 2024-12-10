import time

from lib.colour_tools import just_an_rgb, scale_colour
from lib.context import pixels
from lib.orderings import get_pairs
from lib.tools import colour_pair, inverse_square_tail, rotate_list


def wave():
    """Waves of colour."""
    sleep_time = 10
    sequence = get_pairs("left", "w") + get_pairs("right", "w")
    values = inverse_square_tail(len(sequence))

    while True:
        colour = just_an_rgb()
        for index, value in enumerate(values):
            colour_pair(pixels, sequence[index], scale_colour(colour, value))

            pixels.write()

        values = rotate_list(values, direction="l")
        time.sleep_ms(sleep_time)
