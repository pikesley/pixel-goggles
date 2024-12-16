from lib.colour_tools import spectrum
from lib.eye import Eye
from tests.helpers.fake_pixels import FakePixels

pixels = FakePixels(16)

eye = Eye(pixels, "left")
eye.load_ordering(point="n", rotation="pairs")
eye.load_ordering(point="s")

colours = spectrum(16)

eye.fill(colours)
