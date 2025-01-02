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
    "service": "a29b77fe-e208-40d4-aa7a-6abda275844b",
    "pattern": "266517c5-cf1c-4f86-a1fc-0dca0066562e",
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
