from machine import Pin, SoftI2C

i2c = SoftI2C(sda=Pin(9), scl=Pin(8), freq=400000)
device = 0x3E

size = {"x": 240, "y": 135}


def initialise(background_colour=(0, 0, 0)):
    """Clear screen."""
    b = bytearray(1)

    # turn screen on
    b[0] = 255
    i2c.writeto_mem(device, 0x22, b)

    # disable colour inversion
    b[0] = 0
    i2c.writeto_mem(device, 0x20, b)

    # rotate screen
    b[0] = 1
    i2c.writeto_mem(device, 0x36, b)

    fill_screen(background_colour)


def fill_screen(colour):
    """Fill the screen with `(r, g, b)`."""
    draw_rect(0, 0, size["x"], size["y"], colour)


def draw_rect(x_left, y_top, x_right, y_bottom, colour):
    """Draw a rectangle."""
    command = 0x6B
    i2c.writeto_mem(
        device,
        command,
        bytearray([x_left, y_top, x_right, y_bottom, colour[0], colour[1], colour[2]]),
    )
