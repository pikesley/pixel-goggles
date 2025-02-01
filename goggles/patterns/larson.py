import asyncio
import gc

from lib.colour_tools import just_an_rgb, scale_colour
from lib.context import goggles, pixels
from lib.tools import get_intervals, inverse_square_tail


async def larson():
    """Knightrider."""
    sleep_multiplier = 50
    length = 36
    values = inverse_square_tail(length, coefficient=0.5, backwards=True)
    intervals = get_intervals(sleep_multiplier)

    directions = {
        "w": (goggles.left, goggles.right),
        "e": (goggles.right, goggles.left),
    }

    while True:
        for direction, sides in directions.items():
            goggles.load_ordering(point=direction, rotation="pairs")
            for _ in range(len(values)):
                colour = just_an_rgb()
                colours = [scale_colour(colour, v) for v in values]

                for index, offset in enumerate([0, 9]):
                    sides[index].fill(colours[offset:])

                pixels.write()

                await asyncio.sleep_ms(int(intervals.head))
                intervals.rotate()
                values.rotate(direction="r")
                gc.collect()
