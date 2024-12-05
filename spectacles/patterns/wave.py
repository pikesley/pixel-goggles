import time

from lib.colour_tools import rgb_from_hue, scale_colour
from lib.context import brightness, hue_source, pixels


def wave():
    """Waves of colour."""
    sleep_time = 40
    offset = 0

    index_pairs = [
        ((i + offset) % len(pixels), ((len(pixels) - i - 1) + offset) % len(pixels))
        for i in range(int(len(pixels) / 2))
    ]

    count = 0
    while True:
        colour_source = rgb_from_hue(hue_source.hue())

        colour = colour_source["bytes"]
        if count == 1:
            colour = colour_source["inverse"]

        scaled_colour = scale_colour(colour, brightness)

        # index_pairs.reverse()

        for pair in index_pairs:
            for item in pair:
                pixels[item] = scaled_colour

            pixels.write()
            time.sleep_ms(sleep_time)

        count = (count + 1) % 2
