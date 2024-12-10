from lib.colour_tools import just_an_rgb, scale_colour
from lib.context import brightness, pixels
from lib.orderings import get_pairs
from lib.tools import colour_pair, rotate_list


def slider():
    """Slide across."""
    left = get_pairs("left", "e")
    right = get_pairs("right", "e")
    sequence = left + right
    bands = [0] * len(left) + [brightness] * len(left)
    direction = "l"

    while True:
        for index, pair in enumerate(sequence):
            colour_pair(pixels, pair, scale_colour(just_an_rgb(), bands[index]))

            pixels.write()

        bands = rotate_list(bands, direction=direction)
