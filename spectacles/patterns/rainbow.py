import time

from lib.colour_tools import rgb_from_degrees, scale_colour
from lib.context import brightness, pixels
from lib.orderings import get_ordering


def rainbow():
    """Spin the wheel."""
    interval = 360 / 16

    colours = [
        scale_colour(rgb_from_degrees(i * interval)["bytes"], brightness)
        for i in range(16)
    ]

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
        colours = [colours[-1]] + colours[:-1]

        time.sleep_ms(sleep_time)
