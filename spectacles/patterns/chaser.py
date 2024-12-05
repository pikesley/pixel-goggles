import time

from lib.colour_tools import rgb_from_hue, scale_colour
from lib.context import brightness, hue_source, pixels


def chaser():
    """Chase around the wheel."""
    sleep_time = 40

    indeces = list(range(len(pixels)))

    while True:
        for index, scale_index in enumerate(indeces):
            hue = hue_source.hue()
            colour = rgb_from_hue(hue)["bytes"]
            pixels[index] = scale_colour(
                # pixels[len(pixels) - 1 - index] = scale_colour(
                colour,
                (scale_index / len(pixels)) * brightness,
            )
            pixels.write()

        time.sleep_ms(sleep_time)
        indeces = [indeces[-1]] + indeces[:-1]
