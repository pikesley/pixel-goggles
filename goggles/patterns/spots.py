import asyncio
import gc
from math import ceil, floor
from random import randint

from lib.colour_tools import just_an_rgb
from lib.context import goggles, pixels, ring_size
from lib.tools import cos_curve, random_rotation


async def spots():
    """Spots."""
    spots = randint(2, 5)  # noqa: S311

    interval_divider = 5
    intervals = cos_curve(interval_divider)

    direction = random_rotation()
    outer_range = range(int(ring_size / spots), 0, -1)

    if "anti" in direction:
        outer_range = range(int(ring_size / spots))

    while True:
        colour = just_an_rgb()

        for i in outer_range:
            goggles.off()

            for k in range(spots):
                goggles.left[(get_rounding(k, spots, i))] = colour
                goggles.right[(get_rounding(k, spots, i))] = colour

            pixels.write()
            await asyncio.sleep_ms(int(intervals.head * 1000))
            intervals.rotate()
            gc.collect()


def get_rounding(k, spots, i):
    """`floor` or `ceil`."""
    rounding_method = floor if randint(0, 1) == 1 else ceil  # noqa: S311

    return rounding_method(k * (16 / spots)) + i
