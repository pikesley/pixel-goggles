# https://github.com/DFRobot/micropython-dflib/blob/master/ADXL345/user_lib/ADXL345.py

from machine import Pin, SoftI2C

from lib.context import pins

device = 0x53
reg_address = 0x32
TO_READ = 6
buff = bytearray(6)
i2c = SoftI2C(sda=Pin(pins["sda"]), scl=Pin(pins["scl"]), freq=400000)

limits = {
    "x": {"anticlockwise": -235, "clockwise": 270},
    "y": {"horizontal": 0, "vertical": 260},
}


class ADXL345:
    """Tilt sensor."""

    def __init__(self, i2c=i2c, addr=device):
        """Construct."""
        self.addr = addr
        self.i2c = i2c

    def read_value(self, index):
        """Read some data."""
        buff = self.buff()
        data = (int(buff[index + 1]) << 8) | buff[index]
        if data > 32767:  # noqa: PLR2004
            data -= 65536
        return data

    @property
    def values(self):
        """Us as a dict."""
        return {
            "x": self.read_value(0),
            "y": self.read_value(2),
            "z": self.read_value(4),
        }

    @property
    def restricted_values(self):
        """Restricted values."""
        vals = self.values

        x = vals["x"]
        x = min(x, limits["x"]["clockwise"])
        x = max(x, limits["x"]["anticlockwise"])

        vals["x"] = x

        y = vals["y"]
        y = min(y, limits["y"]["vertical"])
        y = max(y, limits["y"]["horizontal"])

        vals["y"] = y

        return vals

    def buff(self):
        """Read the data."""
        return self.i2c.readfrom_mem(self.addr, reg_address, TO_READ)
