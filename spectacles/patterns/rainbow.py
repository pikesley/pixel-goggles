import time

from lib.colour_tools import spectrum
from lib.context import pixels
from lib.orderings import get_ordering


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
                pixels[ordering[i]] = colours[i]

        pixels.write()
        colours.rotate()

        time.sleep_ms(sleep_time)
