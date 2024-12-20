import time

import machine

from lib.colour_tools import scale_colour, time_based_rgb
from lib.context import button_pin, goggles, pixels
from lib.tools import inverse_square_tail

pulse_length = 100
sleep_time = 5
tail_coefficient = 0.3
rotate_count = 0
values = inverse_square_tail(pulse_length, coefficient=tail_coefficient)


def responder():
    """Flash with a button."""
    global rotate_count  # noqa: PLW0603

    while True:
        # colour = just_an_rgb()
        colour = time_based_rgb(5)
        goggles.left.fill(scale_colour(colour["bytes"], values.head))
        goggles.right.fill(scale_colour(colour["inverse"], values.head))
        pixels.write()
        time.sleep_ms(sleep_time)
        rotate_count += 1

        if rotate_count < pulse_length:
            values.rotate()


def reset_values(pin):
    """Reset the values."""
    global rotate_count  # noqa: PLW0603
    if pin.value() == 0:
        rotate_count = 0
        values.reset()


switch = machine.Pin(button_pin, machine.Pin.IN)
switch.irq(trigger=machine.Pin.IRQ_RISING, handler=reset_values)
