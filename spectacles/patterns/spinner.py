import time

from lib.colour_tools import rgb_from_hue, scale_colour
from lib.context import brightness, hue_source, pixels
from lib.orderings import get_ordering


def spinner():
    """Spin the wheel."""
    sleep_time = 40
    tail = 8

    left = get_ordering("left", "e", "clockwise", overlap=True)
    right = get_ordering("right", "w", "anticlockwise", overlap=True)
    sequence = left + right

    while True:
        for i in range(len(sequence)):
            colour = scale_colour(rgb_from_hue(hue_source.hue())["bytes"], brightness)

            for t in range(tail):
                pixels[sequence[(i - t)] % len(sequence)] = scale_colour(
                    colour, 1 / (t + 1)
                )

            pixels[sequence[(i - t)] % len(sequence)] = (0, 0, 0)

            pixels.write()
            time.sleep_ms(sleep_time)
