from machine import Pin, SoftI2C

i2c = SoftI2C(sda=Pin(9), scl=Pin(8), freq=400000)
device = 0x3E

size = {
    "x": 240,
    "y": 135
}

def initialise():
    """Clear screen."""
    b = bytearray(1)

    # turn screen on
    b[0] = 255
    i2c.writeto_mem(device, 0x22, b)

    # invert colours
    b[0] = 1
    i2c.writeto_mem(device, 0x20, b)

    # rotate screen
    b[0] = 1
    i2c.writeto_mem(device, 0x36, b)

    fill_screen((255, 255, 255))

def fill_screen(colour):
    """Fill the screen with `(r, g, b)`."""
    command = 0x6B
    i2c.writeto_mem(
        device,
        command,
        bytearray(
            [0, 0, size["x"], size["y"], colour[0], colour[1], colour[2]]
        )
    )


initialise()
fill_screen((255, 0, 0))
