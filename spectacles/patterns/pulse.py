import time

from lib.colour_tools import scale_colour, time_based_rgb
from lib.context import pixels
from lib.orderings import get_ordering
from lib.tools import inverse_square_tail


def pulse():
    """Pulse."""
    pulse_length = 100
    sleep_time = 5

    left = get_ordering("left", "n")
    right = get_ordering("right", "n")

    left_values = inverse_square_tail(pulse_length, coefficient=0.07)
    right_values = inverse_square_tail(pulse_length, coefficient=0.07)

    right_values.rotate(steps=int(len(left_values) / 4), direction="r")

    while True:
        colour = time_based_rgb(1.2)

        for i in range(len(left_values)):
            for index in range(len(left)):
                pixels[left[index]] = scale_colour(colour["bytes"], left_values[i])
                pixels[right[index]] = scale_colour(colour["inverse"], right_values[i])

            pixels.write()
            time.sleep_ms(sleep_time)
