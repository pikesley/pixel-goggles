import os

pins = {
    "data": 1,
    "button": 0,
    "sda": 9,  # mauve
    "scl": 8,  # green
}

leds = 32
ring_size = 16

defaults = {"brightness": 1.0, "seconds-per-hue-rotation": 50}

if os.uname().sysname == "esp32":
    import machine
    import neopixel

    from lib.eye import Eye
    from lib.goggles import Goggles

    pixels = neopixel.NeoPixel(machine.Pin(pins["data"]), leds)
    length = len(pixels)

    on_board = machine.Pin(8, machine.Pin.OUT)

    eyes = {
        "left": Eye(pixels, "left"),
        "right": Eye(pixels, "right"),
    }

    goggles = Goggles(pixels)
