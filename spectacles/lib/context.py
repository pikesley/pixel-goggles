import os

from lib.time_based_hue_source import TimeBasedHueSource

pin = 10
leds = 32
brightness = 1
seconds_per_rotation = 50

if os.uname().sysname == "esp32":
    import machine
    import neopixel

    pixels = neopixel.NeoPixel(machine.Pin(pin), leds)
    length = len(pixels)


hue_source = TimeBasedHueSource(seconds_per_rotation)
