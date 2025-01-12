import asyncio
import gc
from random import randint

from lib.colour_tools import rgb_from_hue
from lib.compass_points import compass_points
from lib.context import eyes, pixels
from lib.random_hue_source import RandomHueSource


async def wiper():
    """Wipe colours."""
    sides = ["left", "right"]
    hue_sources = {
        "left": RandomHueSource(),
        "right": RandomHueSource(),
    }

    sleep_limits = (5, 30)

    while True:
        side = sides[randint(0, 1)]  # noqa: S311
        eye = eyes[side]
        point = random_point()
        colour = rgb_from_hue(hue_sources[side].hue())["bytes"]
        sleep_time = randint(*sleep_limits)  # noqa: S311

        await populate_eye(eye, point, colour, sleep_time)

        gc.collect()


async def populate_eye(eye, point, colour, sleep_time):
    """Populate an eye."""
    eye.load_ordering(point=point, rotation="pairs")

    for i in range(9):
        eye.set_pair(i, colour)

        pixels.write()
        await asyncio.sleep_ms(sleep_time)


def random_point():
    """Get random compass point."""
    return compass_points[randint(0, len(compass_points) - 1)]  # noqa: S311
