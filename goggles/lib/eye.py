from collections import OrderedDict


class Eye:
    """One eye of a goggle."""

    def __init__(self, pixels, side, north_index, leds=16):
        """Construct."""
        self.pixels = pixels
        self.side = side
        self.north_index = north_index
        self.leds = leds

        self.assign_compass()

    def assign_compass(self):
        """Assign compass points."""
        self.compass = OrderedDict()
        for index, point in enumerate(compass_points):
            self.compass[point] = (index + self.north_index) % self.leds


class FakePixels(list):
    """Fake NeoPixels for testing."""

    def __init__(self, length=16):
        """Construct."""
        self.length = length
        for _ in range(self.length):
            self.append((0, 0, 0))


compass_points = [
    "n",
    "nnw",
    "nw",
    "wnw",
    "w",
    "wsw",
    "sw",
    "ssw",
    "s",
    "sse",
    "se",
    "ese",
    "e",
    "ene",
    "ne",
    "nne",
]
