import time

from lib.colour_tools import scale_colour, scaled_rgb
from lib.context import pixels
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
            colour = scaled_rgb()

            for t in range(tail):
                pixels[sequence[(i - t)] % len(sequence)] = scale_colour(
                    colour, 1 / (t + 1)
                )

            pixels[sequence[(i - t)] % len(sequence)] = (0, 0, 0)

            pixels.write()
            time.sleep_ms(sleep_time)
