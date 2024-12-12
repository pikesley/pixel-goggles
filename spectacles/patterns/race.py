import time

from lib.colour_tools import scale_colour, time_based_rgb
from lib.context import pixels
from lib.orderings import get_ordering
from lib.tools import cos_curve, inverse_square_tail


def race():
    """Spin the wheel."""
    interval_divider = 50

    left = get_ordering("left", "e", "clockwise", overlap=False)
    right = get_ordering("right", "e", "clockwise", overlap=False)

    values = inverse_square_tail(len(left), coefficient=0.5, backwards=True)
    intervals = cos_curve(interval_divider)

    while True:
        for i in range(len(left)):
            colour = time_based_rgb()
            pixels[left[i]] = scale_colour(colour["bytes"], values[i])
            pixels[right[i]] = scale_colour(colour["inverse"], values[i])

        pixels.write()
        time.sleep(intervals.head)

        intervals.rotate()
        values.rotate(direction="r")
