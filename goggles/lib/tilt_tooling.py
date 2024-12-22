from lib.compass_points import compass_points
from lib.fancy_list import FancyList

distances = [
    1.0,
    0.8086582838174551,
    0.6464466094067263,
    0.5380602337443566,
    0.5,
    0.46193976625564337,
    0.3535533905932738,
    0.19134171618254492,
    0,
    0.19134171618254492,
    0.3535533905932738,
    0.46193976625564337,
    0.5,
    0.5380602337443566,
    0.6464466094067263,
    0.8086582838174551,
]

base_values = [
    -1.125,
    -0.875,
    -0.625,
    -0.375,
    -0.125,
    0.125,
    0.375,
    0.625,
    0.875,
    1.125,
]


def filled_points(top, proportion):
    """Work out which points are filled."""
    filled = []
    for point, distance in locate_points(top).items():
        if distance <= proportion:
            filled.append(point)

    return filled


def locate_points(top):
    """Work out how far points are from the bottom."""
    fancy_points = FancyList(compass_points)
    fancy_points.rotate_until(top)
    return dict(zip(fancy_points, distances, strict=False))


# def rotation_lookups(anticlockwise_limit, clockwise_limit):
#     """Assign compass-points to rotations."""
#     fancy_points = FancyList(compass_points)
#     fancy_points.reverse()
#     fancy_points.rotate_until("w")

#     span = (clockwise_limit - anticlockwise_limit) + 1
#     lookups = {}
#     for i in range(span):
#         point = fancy_points[ceil(i * interval)]
#         lookups[anticlockwise_limit + i] = point


def assign_ranges(anticlockwise_limit, clockwise_limit):
    """Assign ownership of ranges to compass-points."""
    fancy_points = FancyList(compass_points.copy())
    fancy_points.reverse()
    fancy_points.rotate_until("w")

    multiplier = (clockwise_limit - anticlockwise_limit) / 2

    ranges = {}
    for i in range(len(base_values) - 1):
        ranges[fancy_points[i]] = (
            base_values[i] * multiplier,
            base_values[i + 1] * multiplier,
        )

    return ranges
