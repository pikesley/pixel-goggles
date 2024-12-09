import time

from lib.colour_tools import just_an_rgb, scale_colour
from lib.context import pixels
from lib.orderings import get_pairs


def wave():
    """Waves of colour."""
    sleep_time = 10
    tail = 8
    sequence = get_pairs("left", "w") + get_pairs("right", "w")

    values = [0] * len(sequence)

    for t in range(tail):
        values[t - 1] = 1 / (2**t)

    while True:
        colour = just_an_rgb()
        for index, value in enumerate(values):
            for member in sequence[index]:
                pixels[member] = scale_colour(colour, value)

            pixels.write()
        values = [values[-1]] + values[:-1]
        time.sleep_ms(sleep_time)
