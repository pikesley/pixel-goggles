import asyncio
import gc

from lib.colour_tools import scale_colour, time_based_rgb
from lib.context import eyes, pixels, ring_size
from lib.tools import cos_curve, inverse_square_tail


async def race():
    """Spin the wheel."""
    interval_divider = 50

    values = inverse_square_tail(ring_size, coefficient=0.5, backwards=True)
    intervals = cos_curve(interval_divider)

    while True:
        for _ in range(ring_size):
            colour = time_based_rgb()
            left_colours = [scale_colour(colour["bytes"], v) for v in values]
            right_colours = [scale_colour(colour["inverse"], v) for v in values]

            eyes["left"].fill(left_colours)
            eyes["right"].fill(right_colours)

            pixels.write()
            await asyncio.sleep_ms(int(intervals.head * 1000))

            intervals.rotate()
            values.rotate(direction="r")
            gc.collect()
