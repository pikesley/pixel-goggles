from lib.context import pixels


def calibration_cross():
    """Make the calibration cross."""
    for i in range(32):
        pixels[i] = (0, 0, 0)

    pixels[14] = (0, 0, 255)
    pixels[6] = (0, 0, 255)
    pixels[2] = (0, 0, 255)
    pixels[26] = (0, 0, 255)
    pixels[30] = (0, 0, 255)
    pixels[18] = (0, 0, 255)

    pixels[10] = (255, 0, 0)
    pixels[22] = (255, 0, 0)
    pixels.write()
