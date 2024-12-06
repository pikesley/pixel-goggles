import time

from lib.colour_tools import rgb_from_hue, scale_colour
from lib.context import brightness, hue_source, length, pixels
from lib.indexing_tools import intensity_list


def spectacle_roller():
    """Roll around the glasses."""
    sleep_time = 40
    indeces = [0] + list(range(15, 0, -1)) + list(range(29, 32)) + list(range(16, 29))  # noqa: RUF005
    brightnesses = intensity_list(length)

    while True:
        for i in indeces:
            pixels[indeces[i]] = scale_colour(
                rgb_from_hue(hue_source.hue())["bytes"], brightness * brightnesses[i]
            )
        pixels.write()
        time.sleep_ms(sleep_time)

        indeces = [indeces[-1]] + indeces[:-1]
