from lib.colour_tools import spectrum
from lib.context import goggles, pixels
from lib.tilt_sensor import ADXL345, limits
from lib.tilt_tooling import rotation_lookups

lookups = rotation_lookups(limits["x"]["anticlockwise"], limits["x"]["clockwise"])

spectrum = spectrum(16)


def tilting_rainbow():
    """Tilt."""
    tilt_sensor = ADXL345()

    while True:
        x = tilt_sensor.restricted_values["x"]

        goggles.left.load_ordering(point=lookups[x], rotation="clockwise")
        goggles.right.load_ordering(point=lookups[x], rotation="clockwise")

        goggles.left.fill(spectrum)
        goggles.right.fill(spectrum)

        pixels.write()
