import os

pins = {
    "data": 1,  # green
    "button": 0,
    "sda": 9,  # mauve
    "scl": 8,  # green
}

# 3.3v pin: yellow, from button

leds = 32
ring_size = 16

defaults = {"brightness": 1.0, "seconds-per-hue-rotation": 50}

bluetooth_uuids = {
    "service": "6a074824-cdf1-44df-b577-d4015cb2f8f3",
    "pattern": "f880be7a-8265-478a-8409-e68ca1d81c4f",
}

# allow importing of `patterns` elsewhere
goggles = None
pixels = None
eyes = None

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
