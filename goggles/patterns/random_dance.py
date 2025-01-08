import asyncio
import gc
from random import randint, random

from lib.colour_tools import rgb_from_hue, scale_colour
from lib.context import eyes, goggles, pixels, ring_size


async def random_dance():
    """Horrors."""
    max_active_dots = 2
    time_range = (10, 100)

    degeneracy_thresholds = {
        "direction": 0.9,
        "colour": 0.99,
        "chaos": 0.99,
    }

    while True:
        goggles.off()
        for _ in range(randint(1, max_active_dots)):  # noqa: S311
            colour = rgb_from_hue(random())  # noqa: S311
            parameters = {
                "direction": "n",
                "index": randint(0, ring_size - 1),  # noqa: S311
                "colour": colour["bytes"],
                "value": random(),  # noqa: S311
            }

            populate(eyes["left"], parameters)

            if random() > degeneracy_thresholds["direction"]:  # noqa: S311
                parameters["direction"] = "s"
            if random() > degeneracy_thresholds["colour"]:  # noqa: S311
                parameters["colour"] = colour["inverse"]
            if random() > degeneracy_thresholds["chaos"]:  # noqa: S311
                parameters["index"] = randint(0, ring_size - 1)  # noqa: S311
                parameters["colour"] = rgb_from_hue(random())["bytes"]  # noqa: S311
                parameters["value"] = random()  # noqa: S311

            populate(eyes["right"], parameters)

        pixels.write()
        await asyncio.sleep_ms(randint(*time_range))  # noqa: S311
        gc.collect()


def populate(eye, parameters):
    """Fill the eye."""
    eye.load_ordering(parameters["direction"])
    eye[parameters["index"]] = scale_colour(parameters["colour"], parameters["value"])
