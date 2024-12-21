from lib.compass_points import compass_points
from lib.fancy_list import FancyList

fancy_points = FancyList(compass_points)
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


def filled_points(top, proportion):
    """Work out which points are filled."""
    filled = []
    for point, distance in locate_points(top).items():
        if distance <= proportion:
            filled.append(point)

    return filled


def locate_points(top):
    """Work out how far points are from the bottom."""
    fancy_points.rotate_until(top)
    return dict(zip(fancy_points, distances, strict=False))
