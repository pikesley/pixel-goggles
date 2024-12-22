import time

from lib.tilt_sensor import tilt_sensor
from lib.tilt_tooling import rotation_lookups, filled_points
from lib.context import goggles, pixels
from lib.colour_tools import just_an_rgb

# I think the device might need calibrating
limits = {"x": {"anti-clockwise": -235, "clockwise": 270}}
lookups = rotation_lookups(limits["x"]["anti-clockwise"], limits["x"]["clockwise"])

proportion = 0.5


def tilter():
    """Tilt."""
    while True:
        x = tilt_sensor.x_val
        x = min(x, limits["x"]["clockwise"])
        x = max(x, limits["x"]["anti-clockwise"])

        points = filled_points(lookups[x], proportion)

        colour = just_an_rgb()
        goggles.off()

        for point in points:
            goggles.left[point] = colour
            goggles.right[point] = colour

        pixels.write()
