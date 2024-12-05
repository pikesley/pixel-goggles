import time

from lib.colour_tools import rgb_from_hue, scale_colour
from lib.context import brightness, hue_source, pixels
from lib.tools import index_pairs


def wave():
    """Waves of colour."""
    sleep_time = 40
    offset = 0

    pairs = index_pairs(len(pixels), offset)

    count = 0
    while True:
        colour_source = rgb_from_hue(hue_source.hue())

        colour = colour_source["bytes"]
        if count == 1:
            colour = colour_source["inverse"]

        scaled_colour = scale_colour(colour, brightness)

        for pair in pairs:
            for item in pair:
                pixels[item] = scaled_colour

            pixels.write()
            time.sleep_ms(sleep_time)

        count = (count + 1) % 2
