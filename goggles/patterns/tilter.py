from lib.colour_tools import just_an_rgb
from lib.context import goggles, pixels
from lib.tilt_sensor import initialise, limits, values
from lib.tilt_tooling import filled_points, rotation_lookups

lookups = rotation_lookups(limits["x"]["anticlockwise"], limits["x"]["clockwise"])

proportion = 0.6


async def tilter():
    """Tilt."""
    initialise()

    while True:
        x = values()["x"]
        # y = restricted_values()["y"]
        # proportion = (y / limits["y"]["vertical"]) * proportion_multiplier

        points = filled_points(lookups[x], proportion)

        colour = just_an_rgb()
        goggles.off()

        for point in points:
            goggles.left[point] = colour
            goggles.right[point] = colour

        pixels.write()
