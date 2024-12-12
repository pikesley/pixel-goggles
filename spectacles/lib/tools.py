from math import cos, radians

from lib.colour_tools import just_an_rgb
from lib.rotatable_list import RotatableList


def get_intervals(multiplier):
    """Get the timing intervals."""
    timing_intervals = [
        0,
        0.03806,
        0.10839,
        0.16221,
        0.19134,
        0.19134,
        0.16221,
        0.10839,
        0.03806,
    ]

    return RotatableList([int(t * multiplier) for t in timing_intervals])


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

    return RotatableList(values)


def cos_curve(divider):
    """Get `cos` intervals."""
    return RotatableList([(cos(radians(t)) + 1) / divider for t in range(360)])
