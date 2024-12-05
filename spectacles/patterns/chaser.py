import time

from lib.colour_tools import rgb_from_hue, scale_colour
from lib.context import brightness, hue_source, length, pixels


def chaser():
    """Chase around the wheel."""
    sleep_time = 40
    direction = "clockwise"

    indeces = list(range(length))

    while True:
        for index, scale_index in enumerate(indeces):
            hue = hue_source.hue()
            colour = rgb_from_hue(hue)["bytes"]

            pixel_index = index
            if "anti" in direction:
                pixel_index = length - index - 1

            pixels[pixel_index] = scale_colour(
                colour,
                (scale_index / length) * brightness,
            )
            pixels.write()

        time.sleep_ms(sleep_time)
        indeces = [indeces[-1]] + indeces[:-1]
