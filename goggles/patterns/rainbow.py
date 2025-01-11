import asyncio
import gc

from lib.colour_tools import spectrum
from lib.context import eyes, pixels, ring_size


async def rainbow():
    """Spin the wheel."""
    config = {
        "left": {
            "colours": spectrum(ring_size),
            "direction": "n",
            "rotation": "l",
            "steps": 1,
        },
        "right": {
            "colours": spectrum(ring_size),
            "direction": "s",
            "rotation": "r",
            "steps": 1,
        },
    }

    sleep_time = 30

    for side, data in config.items():
        eyes[side].load_ordering(point=data["direction"])

    while True:
        for side, data in config.items():
            eyes[side].fill(data["colours"])

        pixels.write()

        for data in config.values():
            data["colours"].rotate(direction=data["rotation"], steps=data["steps"])

        await asyncio.sleep_ms(sleep_time)
        gc.collect()
