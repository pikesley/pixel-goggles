# ruff: noqa
import json
from random import randint

from lib.colour_tools import time_based_rgb
from lib.fancy_list import FancyList
from lib.font_tools import (
    bytes_to_bits,
    scale_bits,
    assemble_string,
    flatten,
    colour_bits,
    run_length_encode,
)
from lib.screen import device, draw_rect, i2c, initialise, size

file = open("conf/font.json")  # noqa: SIM115, PTH123
chars = json.loads(file.read())

initialise()

text = "© 1982"
scale_factor = 4
characters = []
for character in list(text):
    characters.append(scale_bits(bytes_to_bits(chars[character]), scale_factor))

string = assemble_string(*characters)
coloured = colour_bits(string, 28, 0)
flattened = flatten(coloured)
encoded = run_length_encode(flattened)

i2c.writeto_mem(
    device,
    0x2B,
    bytearray([46, 77]),
)

i2c.writeto_mem(
    device,
    0x2A,
    bytearray([10, 9 + (len(text) * 8 * scale_factor)]),
)

i2c.writeto_mem(device, 0x49, bytearray(encoded))
