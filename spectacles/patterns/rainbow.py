import time

from lib.colour_tools import rgb_from_degrees, scale_colour
from lib.context import brightness, length, pixels
from lib.tools import rotation_index


def rainbow():
    """Spin the wheel."""
    interval = 360 / length
    offset = 0
    sleep_time = 80

    direction = "clockwise"

    while True:
        for i in range(length):
            pixels[rotation_index(i, offset, length, direction=direction)] = (
                scale_colour(
                    rgb_from_degrees(i * interval)["bytes"],
                    brightness,
                )
            )

        pixels.write()
        offset += 1

        time.sleep_ms(sleep_time)
