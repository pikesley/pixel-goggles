import time

from lib.colour_tools import rgb_from_degrees, scale_colour
from lib.context import brightness, pixels
from lib.orderings import get_pairs


def rainbow_wave():
    """Waves of colour."""
    sleep_time = 30
    sequence = get_pairs("right", "e") + get_pairs("left", "e")

    interval = 360 / len(sequence)
    colours = [
        scale_colour(rgb_from_degrees(i * interval)["bytes"], brightness)
        for i in range(len(sequence))
    ]

    while True:
        for index, colour in enumerate(colours):
            for member in sequence[index]:
                pixels[member] = colour

            pixels.write()

        colours = [colours[-1]] + colours[:-1]
        time.sleep_ms(sleep_time)
