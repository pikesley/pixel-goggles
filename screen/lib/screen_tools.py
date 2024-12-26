from math import floor


def rgb_to_332(rgb):
    """Convert a 24-bit (r, g, b) colour to an rgb332 byte."""
    # https://stackoverflow.com/a/25258336
    red = floor(rgb[0] / 32) << 5
    green = floor(rgb[1] / 32) << 2
    blue = floor(rgb[2] / 64)

    return red + green + blue
