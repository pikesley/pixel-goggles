import asyncio
import gc
import json

from lib.colour_tools import rgb_from_degrees
from lib.context import pixels

angles = json.load(open("conf/locations/angles.json"))  # noqa: SIM115, PTH123
gc.collect()

increment = 1
sleep_time = 1


async def smooth():
    """Smooth spinner."""
    offset = 0
    while True:
        for index, angle in enumerate(angles):
            colour = rgb_from_degrees((angle + offset) % 360)
            pixels[index] = colour["bytes"]

        pixels.write()
        offset = (offset + increment) % 360
        gc.collect()

        await asyncio.sleep_ms(sleep_time)
