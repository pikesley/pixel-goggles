import time

from lib.colour_tools import scale_colour, spectrum
from lib.context import brightness, pixels
from lib.orderings import get_pairs


def rainbow_wave():
    """Waves of colour."""
    sleep_time = 30
    sequence = get_pairs("right", "e") + get_pairs("left", "e")

    colours = spectrum(len(sequence))

    while True:
        for index, colour in enumerate(colours):
            for member in sequence[index]:
                pixels[member] = scale_colour(colour, brightness)

            pixels.write()

        colours = [colours[-1]] + colours[:-1]
        time.sleep_ms(sleep_time)
