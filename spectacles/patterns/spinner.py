import time

from lib.colour_tools import rgb_from_hue, scale_colour
from lib.context import brightness, hue_source, pixels
from lib.orderings import orderings


def spinner():
    """Spin the wheel."""
    sleep_time = 60
    tail = 8

    orders = (
        orderings["left-hand"]["clockwise"],
        orderings["right-hand"]["anticlockwise"],
    )

    while True:
        for i in range(16):
            colour = scale_colour(rgb_from_hue(hue_source.hue())["bytes"], brightness)

            for ordering in orders:
                pixels[ordering[(i - tail) % 16]] = (0, 0, 0)
                pixels[ordering[i]] = colour

            pixels.write()
            time.sleep_ms(sleep_time)
