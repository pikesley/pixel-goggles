from lib.colour_tools import just_an_rgb
from lib.context import goggles, pixels
from lib.tilt_sensor import ADXL345
from lib.tilt_tooling import filled_points, rotation_lookups

# I think the device might need calibrating
limits = {
    "x": {"anti-clockwise": -235, "clockwise": 270},
    "y": {"horizontal": 0, "vertical": 260},
}
lookups = rotation_lookups(limits["x"]["anti-clockwise"], limits["x"]["clockwise"])

proportion = 0.6


def tilter():
    """Tilt."""
    tilt_sensor = ADXL345()

    while True:
        x = tilt_sensor.values["x"]
        x = min(x, limits["x"]["clockwise"])
        x = max(x, limits["x"]["anti-clockwise"])

        y = tilt_sensor.values["y"]
        y = min(y, limits["y"]["vertical"])
        y = max(y, limits["y"]["horizontal"])

        # proportion = (y / limits["y"]["vertical"]) * proportion_multiplier

        points = filled_points(lookups[x], proportion)

        colour = just_an_rgb()
        goggles.off()

        for point in points:
            goggles.left[point] = colour
            goggles.right[point] = colour

        pixels.write()
