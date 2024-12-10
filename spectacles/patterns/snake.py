import time

from lib.colour_tools import just_an_rgb, scale_colour
from lib.context import pixels
from lib.orderings import get_ordering


def snake():
    """Spin the wheel."""
    sleep_time = 40
    tail = 10

    left = get_ordering("left", "e", "clockwise", overlap=True)
    right = get_ordering("right", "w", "anticlockwise", overlap=True)
    sequence = left + right

    while True:
        for i in range(len(sequence)):
            colour = just_an_rgb()

            for t in range(tail):
                pixels[sequence[(i - t)] % len(sequence)] = scale_colour(
                    colour, 1 / (t + 1)
                )

            pixels[sequence[(i - t)] % len(sequence)] = (0, 0, 0)

            pixels.write()
            time.sleep_ms(sleep_time)
