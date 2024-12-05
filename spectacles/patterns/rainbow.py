import time

from lib.colour_tools import rgb_from_degrees, scale_colour
from lib.context import brightness, pixels


def rainbow():
    """Spin the wheel."""
    interval = 360 / len(pixels)
    offset = 0
    sleep_time = 80

    while True:
        for i in range(len(pixels)):
            pixels[(i + offset) % len(pixels)] = scale_colour(
                # pixels[len(pixels) - 1 - ((i + offset) % len(pixels))] = scale_colour(
                rgb_from_degrees(i * interval)["bytes"],
                brightness,
            )

        pixels.write()
        offset += 1

        time.sleep_ms(sleep_time)
