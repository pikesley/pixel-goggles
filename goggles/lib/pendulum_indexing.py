from math import pi, sin

from lib.compass_points import compass_points

south_index = compass_points.index("s")


def pendulum_timings(length=16):
    """Get the pendulum timings."""
    timings = [sin((i * pi) / 32) for i in range(1, length, 2)]
    return list(reversed(timings)) + timings


def sequence(offset):
    """Get a sequence."""
    points = compass_points[south_index - offset : south_index + offset + 1]
    intervals = pendulum_timings(length=int(offset * 2))

    return {"points": points, "intervals": intervals}
