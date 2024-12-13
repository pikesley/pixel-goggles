import time

from lib.colour_tools import spectrum
from lib.context import pixels
from lib.orderings import get_ordering, random_origin, random_rotation


def rainbow():
    """Spin the wheel."""
    colours = spectrum(16)

    orderings = (
        get_ordering("left", random_origin(), random_rotation()),
        get_ordering("right", random_origin(), random_rotation()),
    )

    sleep_time = 50

    while True:
        for i in range(16):
            for ordering in orderings:
                pixels[ordering[i]] = colours[i]

        pixels.write()
        colours.rotate()

        time.sleep_ms(sleep_time)
