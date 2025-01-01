import asyncio

from lib.colour_tools import just_an_rgb, scale_colour
from lib.context import goggles, pixels
from lib.tools import get_intervals, inverse_square_tail


async def wave():
    """Waves of colour."""
    sleep_multiplier = 150
    values = inverse_square_tail(27, coefficient=0.5, backwards=True)
    intervals = get_intervals(sleep_multiplier)

    goggles.load_ordering(point="w", rotation="pairs")

    while True:
        colour = just_an_rgb()
        colours = [scale_colour(colour, v) for v in values]

        goggles.left.fill(colours)
        goggles.right.fill(colours[9:])

        pixels.write()

        await asyncio.sleep_ms(int(intervals.head))
        intervals.rotate()
        values.rotate(direction="r")
