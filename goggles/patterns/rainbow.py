import asyncio
import gc

from lib.colour_tools import spectrum
from lib.context import eyes, pixels, ring_size


async def rainbow():
    """Spin the wheel."""
    config = {
        "left": {"colours": spectrum(ring_size), "rotation": "l", "steps": 1},
        "right": {"colours": spectrum(ring_size), "rotation": "r", "steps": 1},
    }

    sleep_time = 30

    while True:
        for side, data in config.items():
            eyes[side].fill(data["colours"])

        pixels.write()

        for data in config.values():
            data["colours"].rotate(direction=data["rotation"], steps=data["steps"])

        await asyncio.sleep_ms(sleep_time)
        gc.collect()
