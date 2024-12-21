import time

from lib.colour_tools import just_an_rgb, scale_colour
from lib.context import goggles, pixels
from lib.fancy_list import FancyList
from lib.pendulum_indexing import sequence
from lib.tools import inverse_square_tail

timing_scale = 200

tail_length = 3
tail = inverse_square_tail(tail_length, coefficient=3)

sequence = sequence(5)
rotations = FancyList(["anticlockwise", "clockwise"])


def pendulum():
    """Spin the wheel."""
    while True:
        rotation = rotations.head
        for i, index in enumerate(sequence["indeces"]):
            colour = just_an_rgb()
            goggles.off()
            for t, value in enumerate(tail):
                goggles.left[offset(index, t, rotation)] = scale_colour(colour, value)
                goggles.right[offset(index, t, rotation)] = scale_colour(colour, value)

            pixels.write()

            try:
                interval = int(sequence["intervals"][i] * timing_scale)
                time.sleep_ms(interval)
            except IndexError:
                pass

        sequence["indeces"].reverse()
        rotations.rotate()


def offset(index, amount, rotation):
    """Offset an index."""
    if rotation == "anticlockwise":
        return index - amount

    return index + amount
