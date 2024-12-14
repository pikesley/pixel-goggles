import time

from lib.colour_tools import just_an_rgb, scale_colour
from lib.context import pixels
from lib.orderings import get_ordering
from lib.tools import inverse_square_tail, off, pendulum_timings


def pendulum():
    """Spin the wheel."""
    offset = 2
    timing_scale = 100

    tail_length = 4

    left = get_ordering("left", "n", "clockwise", overlap=True)[offset:-offset]
    print(left)
    right = get_ordering("right", "n", "clockwise", overlap=True)[offset:-offset]
    timings = pendulum_timings()[offset - 1 : -offset + 1]

    tail = inverse_square_tail(tail_length)

    # while True:
    tail_count = 0
    for i in range(len(left)):
        off(pixels)
        colour = just_an_rgb()

        if tail_count < tail_length:
            tail_count += 1

        for t in range(tail_count):
            tail_index = i - t
            for eye in [left, right]:
                pixels[eye[tail_index]] = scale_colour(colour, tail[t])

        pixels.write()
        interval = int(timings[i] * timing_scale)
        time.sleep_ms(interval)

    while tail_count:
        for eye in [left, right]:
            victim_index = eye[0 - (tail_count)]
            pixels[victim_index] = (0, 0, 0)
        pixels.write()
        tail_count -= 1
        time.sleep_ms(timing_scale)
