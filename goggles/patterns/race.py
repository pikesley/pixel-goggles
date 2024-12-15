import time

from lib.colour_tools import scale_colour, time_based_rgb
from lib.context import eyes, pixels
from lib.tools import cos_curve, inverse_square_tail


def race():
    """Spin the wheel."""
    interval_divider = 5000

    values = inverse_square_tail(16, coefficient=0.5, backwards=True)
    intervals = cos_curve(interval_divider)

    while True:
        for _ in range(16):
            colour = time_based_rgb()
            left_colours = [scale_colour(colour["bytes"], v) for v in values]
            right_colours = [scale_colour(colour["inverse"], v) for v in values]

            eyes["left"].fill(left_colours)
            eyes["right"].fill(right_colours)

        pixels.write()
        time.sleep(intervals.head)

        intervals.rotate()
        values.rotate(direction="r")
