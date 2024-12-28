from math import cos, radians
from random import randint

from lib.fancy_list import FancyList


def get_intervals(multiplier):
    """Get the timing intervals."""
    cosines = [1 - cos(radians((i / 4) * 90)) for i in range(5)]
    intervals = [
        cosines[index + 1] - cosines[index] for index in range(len(cosines) - 1)
    ]
    intervals += list(reversed(intervals))
    intervals += [0]

    return FancyList([int(t * multiplier) for t in intervals])


def inverse_square_tail(length, coefficient=1, backwards=False):  # noqa: FBT002
    """Inverse-square tail-off values."""
    values = [1 / (2 ** (t * coefficient)) for t in range(length)]
    if backwards:
        values.reverse()

    return FancyList(values)


def cos_curve(divider):
    """Get `cos` intervals."""
    return FancyList([(cos(radians(t)) + 1) / divider for t in range(360)])


def off(pixels, write=False):  # noqa: FBT002
    """Turn them all off."""
    for i in range(len(pixels)):
        pixels[i] = (0, 0, 0)

    if write:
        pixels.write()


def is_single_colour(thing):
    """Detect a single colour."""
    return len(thing) == 3  # noqa: PLR2004


def random_rotation():
    """Get a random rotation direction."""
    rotation = "clockwise"
    if randint(0, 1) == 0:  # noqa: S311
        rotation = f"anti{rotation}"

    return rotation
