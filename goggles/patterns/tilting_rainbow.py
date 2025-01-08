import asyncio
import gc

from lib.colour_tools import spectrum
from lib.context import goggles, pixels
from lib.tilt_sensor import initialise, limits, values
from lib.tilt_tooling import rotation_lookups

lookups = rotation_lookups(limits["x"]["anticlockwise"], limits["x"]["clockwise"])

spectrum = spectrum(16)


async def tilting_rainbow():
    """Tilt."""
    initialise()
    sleep_time = 10

    while True:
        x = values()["x"]

        goggles.left.load_ordering(point=lookups[x], rotation="clockwise")
        goggles.right.load_ordering(point=lookups[x], rotation="clockwise")

        goggles.left.fill(spectrum)
        goggles.right.fill(spectrum)

        pixels.write()
        await asyncio.sleep_ms(sleep_time)
        gc.collect()
