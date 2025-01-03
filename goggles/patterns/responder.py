import asyncio
import os

if os.uname().sysname == "esp32":
    import machine

from lib.colour_tools import scale_colour, time_based_rgb
from lib.context import goggles, pins, pixels
from lib.tools import inverse_square_tail

pulse_length = 100
sleep_time = 5
tail_coefficient = 0.3
rotate_count = 0
values = inverse_square_tail(pulse_length, coefficient=tail_coefficient)


async def responder():
    """Flash with a button."""
    global rotate_count  # noqa: PLW0603

    while True:
        colour = time_based_rgb(5)
        goggles.left.fill(scale_colour(colour["bytes"], values.head))
        goggles.right.fill(scale_colour(colour["inverse"], values.head))
        pixels.write()
        await asyncio.sleep_ms(sleep_time)
        rotate_count += 1

        if rotate_count < pulse_length:
            values.rotate()


def reset_values(pin):
    """Reset the values."""
    global rotate_count  # noqa: PLW0603
    if pin.value() == 0:
        rotate_count = 0
        values.reset()


if os.uname().sysname == "esp32":
    switch = machine.Pin(pins["button"], machine.Pin.IN)
    switch.irq(trigger=machine.Pin.IRQ_RISING, handler=reset_values)
