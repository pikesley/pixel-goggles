from math import cos, radians

from lib.colour_tools import just_an_rgb
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


def colour_pair(pixels, pair, colour=None):
    """Apply colour to some indeces."""
    if not colour:
        colour = just_an_rgb()

    for index in pair:
        pixels[index] = colour


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


