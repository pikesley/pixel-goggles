import asyncio

from lib.colour_tools import spectrum
from lib.context import eyes, pixels, ring_size


async def rainbow():
    """Spin the wheel."""
    colours = spectrum(ring_size)
    sleep_time = 30

    for eye in eyes.values():
        eye.load_ordering()

    while True:
        for eye in eyes.values():
            eye.fill(colours)

        pixels.write()
        colours.rotate()
        await asyncio.sleep_ms(sleep_time)
