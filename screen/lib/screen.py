from machine import Pin, SoftI2C

from lib.font_tools import text_data
from lib.screen_tools import (
    horizontal_centering_offsets,
    rgb_to_332,
    size,
    vertical_centering_offsets,
)

i2c = SoftI2C(sda=Pin(9), scl=Pin(8), freq=400000)
device = 0x3E


class ST7789v2:
    """LCD screen."""

    def __init__(
        self,
        i2c=i2c,
        device=device,
        background_colour=0,
        brightness=255,
        invert_colours=False,  # noqa: FBT002
    ):
        """Construct."""
        self.i2c = i2c
        self.device = device
        self.background_colour = background_colour
        self.brightness = brightness
        self.invert_colours = invert_colours

        self.turn_on()
        self.set_inversion()
        self.rotate()
        self.clear_screen()

    def turn_on(self):
        """Turn screen on."""
        self.send_command(0x22, self.brightness)

    def rotate(self, rotation_type=1):
        """Rotate screen."""
        self.send_command(0x36, rotation_type)

    def set_inversion(self):
        """Set colour inversion."""
        command = 0x20
        if self.invert_colours:
            command = 0x21

        self.send_command(command, 0)

    def clear_screen(self):
        """Start again."""
        self.fill_screen(self.background_colour)

    def fill_screen(self, colour):
        """Fill the screen with colour."""
        self.draw_rect(0, 0, size["x"], size["y"], colour)

    def draw_rect(self, x_left, y_top, x_right, y_bottom, colour):
        """Draw a rectangle."""
        if not isinstance(colour, int):
            colour = rgb_to_332(colour)

        self.send_command(0x69, [x_left, y_top, x_right, y_bottom, colour])

    def send_command(self, command, data):
        """Send a command."""
        if not isinstance(data, list):
            data = [data]

        self.i2c.writeto_mem(self.device, command, bytearray(data))

    def write_text(self, text, x, y, colour, scale_factor=2):
        """Write the text at (x, y)."""
        offset = scale_factor * 8

        # TODO pull this out
        if not isinstance(colour, int):
            colour = rgb_to_332(colour)

        x_offsets = (
            horizontal_centering_offsets(text, scale_factor)
            if x == "centered"
            else [x, x + (offset * len(text)) - 1]
        )

        y_offsets = (
            vertical_centering_offsets(scale_factor)
            if y == "centered"
            else [y, y + offset - 1]
        )

        self.send_command(0x2A, x_offsets)
        self.send_command(0x2B, y_offsets)

        data = text_data(text, scale_factor=scale_factor, on_colour=colour, rle=False)
        # 0x49 for RLE
        self.send_command(0x41, data)


screen = ST7789v2()
