import time

from lib.colour_tools import just_an_rgb, scale_colour
from lib.context import eyes, pixels
from lib.tools import get_intervals, inverse_square_tail


def wave():
    """Waves of colour."""
    sleep_multiplier = 50
    values = inverse_square_tail(32)
    intervals = get_intervals(sleep_multiplier)

    while True:
        colour = just_an_rgb()
        for _index, value in enumerate(values):
            for eye in eyes.values():
                for pair in eye.pairwise_iterator("w"):
                    for p in pair:
                        eye[p] = scale_colour(colour, value)

                    # colour_pair(pixels, sequence[index], scale_colour(colour, value))

                    pixels.write()

                    time.sleep_ms(intervals.head)
                    values.rotate()
                    intervals.rotate(direction="r")
