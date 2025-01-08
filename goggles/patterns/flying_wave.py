import asyncio
import gc

from lib.colour_tools import just_an_rgb, scale_colour
from lib.context import goggles, pixels, ring_size
from lib.tools import get_intervals, inverse_square_tail
from lib.wings import Wings


async def flying_wave():
    """Waves of colour."""
    sleep_multiplier = 100

    wings = Wings()

    values = inverse_square_tail(ring_size * 2)
    intervals = get_intervals(sleep_multiplier)

    while True:
        for wing in wings:
            for _ in range(len(values)):
                goggles.left.load_ordering(rotation="pairs", point=wing["left"])
                goggles.right.load_ordering(rotation="pairs", point=wing["right"])

                colour = just_an_rgb()
                colours = [scale_colour(colour, v) for v in values]

                goggles.left.fill(colours)
                goggles.right.fill(colours)

                pixels.write()

                values.rotate()
                intervals.rotate(direction="r")
                await asyncio.sleep_ms(int(intervals.head))
                gc.collect()
