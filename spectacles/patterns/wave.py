import time

from lib.colour_tools import rgb_from_hue, scale_colour
from lib.context import brightness, hue_source, pixels
from lib.orderings import get_pairs


def wave():
    """Waves of colour."""
    sleep_time = 10
    tail = 8
    sequence = get_pairs("left", "w") + get_pairs("right", "w")

    values = [0] * len(sequence)

    for t in range(tail):
        values[t - 1] = 1 / (2 ** t)

    while True:
        colour = rgb_from_hue(hue_source.hue())["bytes"]
        for index, value in enumerate(values):
            for member in sequence[index]:
                pixels[member] = scale_colour(colour, value)

            pixels.write()
        values = [values[-1]] + values[:-1]
        time.sleep_ms(sleep_time)
