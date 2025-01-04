import asyncio
import gc
from random import randint, random

from lib.colour_tools import just_an_rgb, scale_colour
from lib.context import pixels
from lib.tools import inverse_square_tail


async def sparkle():
    """Sparkle."""
    actives = {}

    while True:
        index = randint(0, 31)  # noqa: S311
        actives[index] = inverse_square_tail(randint(10, 100), coefficient=random())  # noqa: S311

        for index, values in actives.items():
            colour = just_an_rgb()
            pixels[index] = scale_colour(colour, values.head)
            values.trim()

            if values.empty():
                pixels[index] = (0, 0, 0)
                del actives[index]

        pixels.write()
        await asyncio.sleep_ms(randint(10, 300))  # noqa: S311
        gc.collect()
