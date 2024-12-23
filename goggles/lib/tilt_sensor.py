# https://github.com/DFRobot/micropython-dflib/blob/master/ADXL345/user_lib/ADXL345.py

from machine import Pin, SoftI2C

device = 0x53
reg_address = 0x32
TO_READ = 6
buff = bytearray(6)
i2c = SoftI2C(sda=Pin(9), scl=Pin(8), freq=400000)


class ADXL345:
    """Tilt sensor."""

    def __init__(self, i2c=i2c, addr=device):
        """Construct."""
        self.addr = addr
        self.i2c = i2c
        b = bytearray(1)
        b[0] = 0
        self.i2c.writeto_mem(self.addr, 0x2D, b)
        b[0] = 16
        self.i2c.writeto_mem(self.addr, 0x2D, b)
        b[0] = 8
        self.i2c.writeto_mem(self.addr, 0x2D, b)

    @property
    def x_val(self):
        """X."""
        buff = self.buff()
        x = (int(buff[1]) << 8) | buff[0]
        if x > 32767:  # noqa: PLR2004
            x -= 65536
        return x

    @property
    def y_val(self):
        """Y."""
        buff = self.buff()
        y = (int(buff[3]) << 8) | buff[2]
        if y > 32767:  # noqa: PLR2004
            y -= 65536
        return y

    @property
    def z_val(self):
        """Z."""
        buff = self.buff()
        z = (int(buff[5]) << 8) | buff[4]
        if z > 32767:  # noqa: PLR2004
            z -= 65536
        return z

    @property
    def values(self):
        """Us as a dict."""
        return {"x": self.x_val, "y": self.y_val, "z": self.z_val}

    def buff(self):
        """Read the data."""
        return self.i2c.readfrom_mem(self.addr, reg_address, TO_READ)
