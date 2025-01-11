import asyncio
import gc
import os

if os.uname().sysname == "esp32":
    import machine


from lib.colour_tools import scale_colour, spectrum
from lib.context import goggles, pins, pixels
from lib.fancy_list import FancyList

pulse_length = 18
values = FancyList([i / 10 for i in [0] * 9 + list(range(10)) + [10] * 9])
values.reverse()

rainbow_length = 48
rainbow = spectrum(rainbow_length)
rainbow.reverse()
rainbow.items = rainbow.items[(rainbow_length - 9) :]

sleep_time = 7
rotate_count = 0


async def dancer():
    """Dance with a button."""
    global rotate_count  # noqa: PLW0603
    goggles.left.load_ordering("sse", rotation="pairs")
    goggles.right.load_ordering("ssw", rotation="pairs")

    while True:
        colours = []
        for index, colour in enumerate(rainbow):
            colours.append(scale_colour(colour, values[index]))

        goggles.left.fill(colours)
        goggles.right.fill(colours)
        pixels.write()
        rotate_count += 1

        if rotate_count <= pulse_length:
            values.rotate()

        await asyncio.sleep_ms(sleep_time)

        gc.collect()


def reset_values(pin):
    """Reset the values."""
    global rotate_count  # noqa: PLW0603

    if pin.value() == 0:
        rotate_count = 0
        values.reset()


if os.uname().sysname == "esp32":
    switch = machine.Pin(pins["button"], machine.Pin.IN)
    switch.irq(trigger=machine.Pin.IRQ_RISING, handler=reset_values)
