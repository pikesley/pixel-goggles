import time

from lib.colour_tools import scale_colour, spectrum
from lib.context import brightness, pixels
from lib.orderings import get_ordering
from lib.tools import rotate_list


def rainbow():
    """Spin the wheel."""
    colours = spectrum(16)

    orderings = (
        get_ordering("left", "n", "clockwise"),
        get_ordering("right", "n", "clockwise"),
    )

    sleep_time = 50

    while True:
        for i in range(16):
            for ordering in orderings:
                pixels[ordering[i]] = scale_colour(colours[i], brightness)

        pixels.write()
        colours = rotate_list(colours, direction="l")

        time.sleep_ms(sleep_time)
