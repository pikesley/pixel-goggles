import asyncio
import gc

from lib.colour_tools import just_an_rgb, scale_colour
from lib.context import eyes, pixels
from lib.tilt_sensor import initialise, limits, values
from lib.tilt_tooling import fade_points, rotation_lookups

lookups = rotation_lookups(limits["z"]["anticlockwise"], limits["z"]["clockwise"])

proportion = 0.6


async def tilter():
    """Tilt."""
    initialise()
    sleep_time = 1

    while True:
        z = values(restricted=True)["z"]
        fades = fade_points(lookups[z], base=3)
        colour = just_an_rgb()

        for point, value in fades.items():
            for side in ["right", "left"]:
                eyes[side][point] = scale_colour(colour, value)

        pixels.write()
        await asyncio.sleep_ms(sleep_time)
        gc.collect()
