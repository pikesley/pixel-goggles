import time

from lib.colour_tools import just_an_rgb
from lib.context import pixels
from lib.orderings import get_ordering
from lib.tools import off, pendulum_timings


def pendulum():
    """Spin the wheel."""
    offset = 2
    timing_scale = 100

    left = get_ordering("left", "n", "clockwise", overlap=True)[offset:-offset]
    right = get_ordering("right", "n", "clockwise", overlap=True)[offset:-offset]
    timings = pendulum_timings()[offset - 1 : -offset + 1]

    while True:
        for i in range(len(left)):
            off(pixels)
            for side in [right, left]:
                colour = just_an_rgb()
                pixels[side[i]] = colour

            pixels.write()
            interval = int(timings[i] * timing_scale)
            time.sleep_ms(interval)

        left = list(reversed(left))
        right = list(reversed(right))
