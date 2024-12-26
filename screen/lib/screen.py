from machine import Pin, SoftI2C

i2c = SoftI2C(sda=Pin(9), scl=Pin(8), freq=400000)
device = 0x3E

size = {"x": 240, "y": 135}

class ST7789v2:
    """LCD screen."""
    def __init__(self, i2c=i2c, device=device, background_colour=(0, 0, 0), brightness=127, invert_colours=False):
        """Construct."""
        self.i2c = i2c
        self.device = device
        self.background_colour = background_colour
        self.brightness = brightness
        self.invert_colours = invert_colours

    def turn_on(self):
        """Turn screen on."""
        self.send_command(0x22, self.brightness)

    def rotate(self, type=1):
        """Rotate screen."""
        self.send_command(0x36, type)

    def set_inversion(self):
        """Set colour inversion."""
        command = 0x20
        if self.invert_colours:
            command = 0x21

        self.send_command(command, 0)

    def fill_screen(self, colour):
        """Fill the screen with `(r, g, b)`."""
        self.draw_rect(0, 0, size["x"], size["y"], colour)


    def draw_rect(self, x_left, y_top, x_right, y_bottom, colour):
        """Draw a rectangle."""
        command = 0x6B
        i2c.writeto_mem(
            device,
            command,
            bytearray([x_left, y_top, x_right, y_bottom, colour[0], colour[1], colour[2]]),
        )

    def send_command(self, command, data):
        """Send a command."""
        self.i2c.writeto_mem(self.device, command, bytearray(data))
