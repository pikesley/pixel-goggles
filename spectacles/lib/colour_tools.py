from math import floor

from lib.context import brightness, hue_source


def get_segments():
    """Get the segments."""
    pattern = [1, None, 0, 0, None, 1]
    offsets = {"red": 0, "blue": 2, "green": 4}

    segments = []
    for i in range(6):
        segments.append({"offset": i * 60})
        for component, offset in offsets.items():
            index = (i + offset) % len(
                pattern
            )  # because `deque` isn't the same in micropython
            if pattern[index] is not None:
                segments[-1][component] = pattern[index]

    return segments


segments = get_segments()


def get_sector(degrees):
    """Determine which sector we're in."""
    return int(floor(degrees / 60))


def rgb_from_degrees(degrees):
    """Get RGB from degrees of rotation."""
    sector = get_sector(degrees % 360)
    segment = segments[sector]
    offset = (1 / 60) * (degrees - segment["offset"])

    if sector % 2 == 1:
        offset = 1 - offset

    rgb = [segment.get(x, offset) for x in ["red", "green", "blue"]]
    return {
        "bytes": tuple([int(x * 255) for x in rgb]),
        "inverse": tuple([255 - int(x * 255) for x in rgb]),
    }


def rgb_from_hue(decimal):
    """Get RGB from hue value (0.0 - 1.0)."""
    return rgb_from_degrees((decimal % 1.0) * 360)


def scale_colour(rgb, factor):
    """Scale a colour."""
    return [int(component * factor) for component in rgb]


def scaled_rgb():
    """Just generate a time-based a colour."""
    return scale_colour(just_an_rgb(), brightness)


def just_an_rgb():
    """Just generate a time-based a colour."""
    return rgb_from_hue(hue_source.hue())["bytes"]
