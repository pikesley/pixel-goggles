import time

from lib.colour_tools import rgb_from_degrees, scale_colour
from lib.context import brightness, pixels
from lib.indexing_tools import rotation_index


def rainbow():
    """Spin the wheel."""
    interval = 360 / 16
    offset = 0
    sleep_time = 50
    left_right_offset = 4

    direction = "anticlockwise"

    while True:
        for i in range(16):
            colour = scale_colour(
                rgb_from_degrees(i * interval)["bytes"],
                brightness,
            )
            rot_index = rotation_index(i, offset, 16, direction=direction)
            pixels[rot_index] = colour
            pixels[((rot_index + left_right_offset) % 16) + 16] = colour

        pixels.write()
        offset += 1

        time.sleep_ms(sleep_time)
