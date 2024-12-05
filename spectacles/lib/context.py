import machine
import neopixel

from conf import leds, pin, seconds_per_rotation
from lib.time_based_hue_source import TimeBasedHueSource

pixels = neopixel.NeoPixel(machine.Pin(pin), leds)
brightness = 0.01
hue_source = TimeBasedHueSource(seconds_per_rotation)
