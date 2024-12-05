import time
from random import randint

from lib.colour_tools import rgb_from_hue, scale_colour
from lib.context import brightness, hue_source, length, pixels


def sparkle():
    """Randomly light up."""
    sleep_time = 80
    max_actives = 10
    active_leds = []

    while True:
        colour = rgb_from_hue(hue_source.hue())["bytes"]

        candidate = randint(0, length - 1)  # noqa: S311
        while candidate not in active_leds:
            candidate = randint(0, length - 1)  # noqa: S311
            active_leds.append(candidate)

        if len(active_leds) > max_actives:
            active_leds = active_leds[1:]

        for index, led_index in enumerate(active_leds):
            pixels[led_index] = scale_colour(
                colour, ((length - index) / length) * brightness
            )

        pixels.write()
        time.sleep_ms(sleep_time)
