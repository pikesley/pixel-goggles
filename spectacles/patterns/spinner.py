import time

from lib.colour_tools import rgb_from_hue, scale_colour
from lib.context import brightness, hue_source, pixels


def spinner():
    """Spin the wheel."""
    segments = 3
    segment = int(len(pixels) / segments)
    sleep_time = 40

    while True:
        hue = hue_source.hue()
        for i in range(segment):
            for j in range(len(pixels)):
                pixels[j] = (0, 0, 0)

            colour = scale_colour(rgb_from_hue(hue)["bytes"], brightness)

            for k in range(segments):
                pixels[i + (segment * k)] = colour

            pixels.write()
            time.sleep_ms(sleep_time)
