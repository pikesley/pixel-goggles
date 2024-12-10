import time
from math import cos, radians

from lib.colour_tools import rgb_from_hue, scale_colour
from lib.context import hue_source, pixels
from lib.orderings import get_ordering
from lib.tools import inverse_square_tail, rotate_list


def spots():
    """Spin the wheel."""
    interval_divider = 50

    left = get_ordering("left", "e", "clockwise", overlap=False)
    right = get_ordering("right", "e", "clockwise", overlap=False)

    values = inverse_square_tail(len(left), coefficient=0.5, backwards=True)
    intervals = [(cos(radians(t)) + 1) / interval_divider for t in range(360)]

    while True:
        for i in range(len(left)):
            colour = rgb_from_hue(hue_source.hue())
            pixels[left[i]] = scale_colour(colour["bytes"], values[i])
            pixels[right[i]] = scale_colour(colour["inverse"], values[i])

        pixels.write()
        time.sleep(intervals[0])
        intervals = rotate_list(intervals)
        values = rotate_list(values, direction="r")
