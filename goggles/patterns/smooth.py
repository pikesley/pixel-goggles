import gc
import json

from lib.colour_tools import rgb_from_degrees
from lib.context import pixels

locations = json.load(open("conf/locations.json"))  # noqa: SIM115, PTH123
gc.collect()
# TODO: load only the angles
increment = 1


async def smooth():
    """Smooth pinner."""
    offset = 0
    while True:
        for pixel in locations:
            colour = rgb_from_degrees((pixel["angle"] + offset) % 360)
            pixels[pixel["index"]] = colour["bytes"]

        pixels.write()
        offset = (offset + increment) % 360
        gc.collect()
