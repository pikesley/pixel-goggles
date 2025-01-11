import json
import os

conf = json.load(open("conf/conf.json"))  # noqa: SIM115, PTH123

pins = conf["pins"]
leds = conf["leds"]
ring_size = conf["ring-size"]
defaults = conf["defaults"]
bluetooth_uuids = conf["bluetooth"]["uuids"]

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
