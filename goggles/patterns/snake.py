import asyncio
import gc

from lib.colour_tools import scale_colour, spectrum
from lib.context import goggles, pixels
from lib.tools import inverse_square_tail


async def snake():
    """Spin the wheel."""
    sleep_time = 25
    colours_offset = 4

    goggles.left.load_ordering(point="e", rotation="clockwise", overlap=True)
    goggles.right.load_ordering(point="w", rotation="anticlockwise", overlap=True)

    ordering = goggles.ordering

    values = inverse_square_tail(len(ordering), backwards=True)
    colours = spectrum(len(ordering) + colours_offset)

    while True:
        for i in range(len(ordering)):
            pixels[ordering[i]] = scale_colour(colours[i], values[i])

        colours.rotate(direction="r")
        values.rotate()

        pixels.write()
        await asyncio.sleep_ms(sleep_time)
        gc.collect()
