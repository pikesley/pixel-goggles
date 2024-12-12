import os

pin = 10
leds = 32

defaults = {"brightness": 0.7, "seconds-per-hue-rotation": 50}

if os.uname().sysname == "esp32":
    import machine
    import neopixel

    pixels = neopixel.NeoPixel(machine.Pin(pin), leds)
    length = len(pixels)
