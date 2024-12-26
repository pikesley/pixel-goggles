from lib.font_tools import get_data
from lib.screen import device, i2c, initialise

initialise()

text = "© 1982 Sinclair Research Ltd."
scale_factor = 1
x_offset = 8

i2c.writeto_mem(
    device,
    0x2B,
    bytearray([66, 77]),
)

i2c.writeto_mem(
    device,
    0x2A,
    bytearray([x_offset, x_offset + (len(text) * 8 * scale_factor) - 1]),
)

i2c.writeto_mem(
    device, 0x49, bytearray(get_data(text, scale_factor=scale_factor, on_colour=0xFC))
)
