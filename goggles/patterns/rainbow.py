import time

from lib.colour_tools import spectrum
from lib.context import eyes, pixels


def rainbow():
    """Spin the wheel."""
    colours = spectrum(16)
    sleep_time = 50

    while True:
        for eye in eyes.values():
            eye.fill(colours)

        pixels.write()
        colours.rotate()
        time.sleep_ms(sleep_time)
