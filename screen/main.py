# ruff: noqa
import json
from random import randint

from lib.colour_tools import time_based_rgb
from lib.fancy_list import FancyList
from lib.font_tools import bytes_to_bits, scale_bits
from lib.screen import device, draw_rect, i2c, initialise, size

file = open("conf/font.json")  # noqa: SIM115, PTH123
chars = json.loads(file.read())

initialise()


def random_blitz():
    """Randomly fill the screen."""
    keys = FancyList(["bytes", "inverse"])

    while True:
        x_vals = [randint(0, size["x"] - 1), randint(0, size["x"] - 1)]
        y_vals = [randint(0, size["y"] - 1), randint(0, size["y"] - 1)]

        x_vals.sort()
        y_vals.sort()
        print(x_vals, y_vals)
        draw_rect(
            x_vals[0], y_vals[0], x_vals[1], y_vals[1], time_based_rgb()[keys.head]
        )
        keys.rotate()


def fix_char(char):
    """Fix char."""
    fixed = []
    bits = scale_bits(bytes_to_bits(chars[char]), 4)
    for line in bits:
        fixed.append([])
        for c in line:
            # 0x41 - rgb332 - 1 byte
            # 0x42 - rgb565 - 2 bytes
            # 0x43 - rgb888 - 3 bytes
            if c == 0:
                fixed[-1].append(0)
                # fixed[-1].append(255)
                # fixed[-1].append(255)
            if c == 1:
                fixed[-1].append(255)
                # fixed[-1].append(0)
                # fixed[-1].append(0)

    return sum(fixed, [])


# text = ["Holy shit it works", " ", "Thank you, Mastodon nerds", " ", "Merry Christmas!"]
text = ["© 1982"]

for i, line in enumerate(text):
    i2c.writeto_mem(
        device,
        0x2B,
        bytearray([46 + (i * 24), 77 + (i * 24)]),
    )

    for index, c in enumerate(line):
        i2c.writeto_mem(
            device,
            0x2A,
            bytearray([26 + (index * 32), 57 + (index * 32)]),
        )

        i2c.writeto_mem(device, 0x41, bytearray(fix_char(c)))

i2c.stop()

# i2c.writeto_mem(
#     device,
#     0x2B,
#     bytearray([10, 17]),
# )

# i2c.writeto_mem(
#     device,
#     0x2A,
#     bytearray([10, 17]),
# )
# [
#     ["0", "0", "0", "0", "0", "0", "0", "0"],
#     ["0", "1", "0", "0", "0", "0", "1", "0"],
#     ["0", "1", "0", "0", "0", "0", "1", "0"],
#     ["0", "1", "1", "1", "1", "1", "1", "0"],
#     ["0", "1", "0", "0", "0", "0", "1", "0"],
#     ["0", "1", "0", "0", "0", "0", "1", "0"],
#     ["0", "1", "0", "0", "0", "0", "1", "0"],
#     ["0", "0", "0", "0", "0", "0", "0", "0"],
# ]

# [
#     "0",
#     "0",
#     "0",
#     "0",
#     "0",
#     "0",
#     "0",
#     "0",
#     "0",
#     "1",
#     "0",
#     "0",
#     "0",
#     "0",
#     "1",
#     "0",
#     "0",
#     "1",
#     "0",
#     "0",
#     "0",
#     "0",
#     "1",
#     "0",
#     "0",
#     "1",
#     "1",
#     "1",
#     "1",
#     "1",
#     "1",
#     "0",
#     "0",
#     "1",
#     "0",
#     "0",
#     "0",
#     "0",
#     "1",
#     "0",
#     "0",
#     "1",
#     "0",
#     "0",
#     "0",
#     "0",
#     "1",
#     "0",
#     "0",
#     "1",
#     "0",
#     "0",
#     "0",
#     "0",
#     "1",
#     "0",
#     "0",
#     "0",
#     "0",
#     "0",
#     "0",
#     "0",
#     "0",
#     "0",
# ]

# data = [
#     9,
#     0,
#     1,
#     255,
#     4,
#     0,
#     1,
#     255,
#     2,
#     0,
#     1,
#     255,
#     4,
#     0,
#     1,
#     255,
#     2,
#     0,
#     6,
#     255,
#     2,
#     0,
#     1,
#     255,
#     4,
#     0,
#     1,
#     255,
#     2,
#     0,
#     1,
#     255,
#     4,
#     0,
#     1,
#     255,
#     2,
#     0,
#     1,
#     255,
#     4,
#     0,
#     1,
#     255,
#     9,
#     0,
# ]

# i2c.writeto_mem(
#     device,
#     0x49,
#     bytearray(data),
# )
