import os

pin = 9
leds = 32

defaults = {"brightness": 1.0, "seconds-per-hue-rotation": 50}

if os.uname().sysname == "esp32":
    import machine
    import neopixel

    pixels = neopixel.NeoPixel(machine.Pin(pin), leds)
    length = len(pixels)

    on_board = machine.Pin(8, machine.Pin.OUT)

    from lib.eye import Eye

    eyes = {
        "left": Eye(pixels, "left"),
        "right": Eye(pixels, "right"),
    }
