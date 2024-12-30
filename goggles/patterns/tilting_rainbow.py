from lib.colour_tools import spectrum
from lib.context import goggles, pixels
from lib.tilt_sensor import limits, values
from lib.tilt_tooling import rotation_lookups

lookups = rotation_lookups(limits["x"]["anticlockwise"], limits["x"]["clockwise"])

spectrum = spectrum(16)


async def tilting_rainbow():
    """Tilt."""
    while True:
        x = values()["x"]

        goggles.left.load_ordering(point=lookups[x], rotation="clockwise")
        goggles.right.load_ordering(point=lookups[x], rotation="clockwise")

        goggles.left.fill(spectrum)
        goggles.right.fill(spectrum)

        pixels.write()
