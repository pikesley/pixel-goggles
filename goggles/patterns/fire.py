import asyncio

from lib.colour_tools import spectrum
from lib.compass_points import compass_points
from lib.context import eyes, goggles, pixels
from lib.fancy_list import FancyList


async def fire():
    """Flames."""
    sleep_time = 200
    rotation_cadence = 20
    rainbow = spectrum(70)
    fancy_points = FancyList(compass_points)

    rotation_count = 0
    while True:
        goggles.off()
        for side in ["left", "right"]:
            eyes[side].load_ordering(point=fancy_points.head, rotation="pairs")
            for index, pair in enumerate(eyes[side]):
                for member in pair:
                    pixels[member] = rainbow[index]

        pixels.write()
        await asyncio.sleep_ms(sleep_time)

        rainbow.rotate()

        rotation_count += 1
        if rotation_count == rotation_cadence:
            rotation_count = 0
            fancy_points.rotate()
