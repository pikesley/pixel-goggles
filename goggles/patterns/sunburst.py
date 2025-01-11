import asyncio
import gc
import json
from math import floor

from lib.colour_tools import spectrum
from lib.context import eyes, pixels
from lib.tools import cos_curve

locations = json.load(open("conf/locations.json"))  # noqa: SIM115, PTH123
gc.collect()

interval_divider = 30
chunk_size = 9

intervals = cos_curve(interval_divider)
gc.collect()

rainbow = spectrum(int(360 / chunk_size))
gc.collect()

sleep_tims = 30


scaled_angles = {
    "left": {},
    "right": {},
}


for pixel in locations:
    scaled_angles[pixel["side"]][pixel["point"]] = floor(pixel["angle"] / chunk_size)


async def sunburst():
    """Sunburst."""
    while True:
        for side, points in scaled_angles.items():
            for point, value in points.items():
                eyes[side][point] = rainbow[value]

        pixels.write()
        await asyncio.sleep_ms(int(intervals.head * 1000))

        rainbow.rotate(direction="l")

        intervals.rotate()
        gc.collect()
