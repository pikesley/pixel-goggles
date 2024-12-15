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
        offset = 0
        if self.side == "right":
            offset = self.leds

        self.compass = OrderedDict()
        for index, point in enumerate(compass_points):
            self.compass[point] = ((index + self.north_index) % self.leds) + offset

    def __setitem__(self, index, colour):
        """Colour a pixel."""
        self.pixels[(index + self.north_index) % self.leds] = colour

    def colour_point(self, point, colour):
        """Colour the pixel at `point`."""
        self.pixels[self.compass[point]] = colour


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
