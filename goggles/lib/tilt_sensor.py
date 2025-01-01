# https://github.com/DFRobot/micropython-dflib/blob/master/ADXL345/user_lib/ADXL345.py

from machine import Pin, SoftI2C

from lib.context import pins

device = 0x53
reg_address = 0x32
TO_READ = 6
buff = bytearray(6)
i2c = SoftI2C(sda=Pin(pins["sda"]), scl=Pin(pins["scl"]), freq=400000)

limits = {
    "x": {"anticlockwise": -235, "clockwise": 260},
    "y": {"horizontal": 0, "vertical": 260},
}


def initialise():
    """Initialise."""
    i2c.writeto_mem(device, 0x2D, bytearray([0]))
    i2c.writeto_mem(device, 0x2D, bytearray([16]))
    i2c.writeto_mem(device, 0x2D, bytearray([8]))


def read_buff():
    """Read the data."""
    return i2c.readfrom_mem(device, reg_address, TO_READ)


def read_value(index):
    """Read some data."""
    buff = read_buff()
    data = (int(buff[index + 1]) << 8) | buff[index]
    if data > 32767:  # noqa: PLR2004
        data -= 65536
    return data


def values(restricted=True):  # noqa: FBT002
    """Get a dict of values."""
    vals = {
        "x": read_value(0),
        "y": read_value(2),
        "z": read_value(4),
    }

    if restricted:
        vals["x"] = min(vals["x"], limits["x"]["clockwise"])
        vals["x"] = max(vals["x"], limits["x"]["anticlockwise"])

        vals["y"] = min(vals["y"], limits["y"]["vertical"])
        vals["y"] = max(vals["y"], limits["y"]["horizontal"])

    return vals
