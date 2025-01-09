import asyncio
import gc
from math import floor

from lib.colour_tools import spectrum
from lib.context import eyes, pixels
from lib.tools import cos_curve

interval_divider = 30
chunk_size = 9

intervals = cos_curve(interval_divider)
gc.collect()

rainbow = spectrum(int(360 / chunk_size))
gc.collect()

sleep_tims = 30

angles = {
    "right": {
        "w": 0.0,
        "wnw": 27.25,
        "nw": 36.38,
        "nnw": 35.73,
        "n": 30.96,
        "nne": 24.26,
        "ne": 16.59,
        "ene": 8.40,
        "e": 0.0,
        "ese": 351.6,
        "se": 343.41,
        "sse": 335.73,
        "s": 329.04,
        "ssw": 324.26,
        "sw": 323.61,
        "wsw": 332.74,
    },
    "left": {
        "e": 180.0,
        "ene": 152.74,
        "ne": 143.61,
        "nne": 144.26,
        "n": 149.03,
        "nnw": 155.73,
        "nw": 163.41,
        "wnw": 171.59,
        "w": 180.0,
        "wsw": 188.40,
        "sw": 196.59,
        "ssw": 204.26,
        "s": 210.96,
        "sse": 215.74,
        "se": 216.38,
        "ese": 207.26,
    },
}

scaled_angles = {
    "left": {},
    "right": {},
}

for side, data in angles.items():
    for point, value in data.items():
        scaled_angles[side][point] = floor(value / chunk_size)


async def sunburst():
    """Sunburst."""
    while True:
        for side, points in scaled_angles.items():
            for point, value in points.items():
                eyes[side][point] = rainbow[value]

        pixels.write()
        # await asyncio.sleep_ms(sleep_tims)
        await asyncio.sleep_ms(int(intervals.head * 1000))

        rainbow.rotate(direction="l")

        intervals.rotate()
        gc.collect()
