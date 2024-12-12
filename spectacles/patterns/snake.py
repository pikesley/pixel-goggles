import time

from lib.colour_tools import scale_colour, spectrum
from lib.context import pixels
from lib.orderings import get_ordering
from lib.tools import inverse_square_tail


def snake():
    """Spin the wheel."""
    sleep_time = 40
    colours_offset = 4

    left = get_ordering("left", "e", "clockwise", overlap=True)
    right = get_ordering("right", "w", "anticlockwise", overlap=True)
    sequence = left + right

    values = inverse_square_tail(len(sequence), backwards=True)
    colours = spectrum(len(sequence) + colours_offset)

    while True:
        for i in range(len(sequence)):
            pixels[sequence[i]] = scale_colour(colours[i], values[i])

        colours.rotate(direction="r")
        values.rotate()

        pixels.write()
        time.sleep_ms(sleep_time)
