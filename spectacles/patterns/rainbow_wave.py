import time

from lib.colour_tools import scale_colour, spectrum
from lib.context import brightness, pixels
from lib.orderings import get_pairs
from lib.tools import colour_pair, rotate_list


def rainbow_wave():
    """Waves of colour."""
    sleep_time = 30
    sequence = get_pairs("right", "e") + get_pairs("left", "e")

    colours = spectrum(len(sequence))

    while True:
        for index, colour in enumerate(colours):
            colour_pair(pixels, sequence[index], scale_colour(colour, brightness))

            pixels.write()

        colours = rotate_list(colours, direction="r")
        time.sleep_ms(sleep_time)
