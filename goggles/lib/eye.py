class Eye:
    """One eye of a goggle."""

    def __init__(self, pixels, side, leds=16):
        """Construct."""
        self.pixels = pixels
        self.side = side
        self.north_index = norths[side]
        self.leds = leds

    def __setitem__(self, index, colour):
        """Colour a pixel."""
        self.pixels[(index + self.north_index) % self.leds] = colour

    def colour_point(self, point, colour):
        """Colour the pixel at `point`."""
        self.pixels[compass_points.index(point)] = colour

    def fill(self, start_point, colours):
        """Fill ourself with a list of colours."""
        start_index = compass_points.index(start_point)

        for index in range(self.leds):
            self[index + start_index] = colours[index]


norths = {"left": 2, "right": 30}

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
