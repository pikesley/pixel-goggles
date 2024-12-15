from lib.fancy_list import FancyList


class Eye:
    """One eye of a goggle."""

    def __init__(self, pixels, side, leds=16):
        """Construct."""
        self.pixels = pixels
        self.side = side
        self.north_index = norths[side]
        self.leds = leds

        self.offset = 0
        if self.side == "right":
            self.offset = self.leds

    def __setitem__(self, index, colour):
        """Colour a pixel."""
        self.pixels[((index + self.north_index) % self.leds) + self.offset] = colour

    def colour_point(self, point, colour):
        """Colour the pixel at `point`."""
        self.pixels[
            ((compass_points.index(point) + self.north_index) % 16) + self.offset
        ] = colour

    def fill(self, colours, start_point="n"):
        """Fill ourself with a list of colours."""
        start_index = compass_points.index(start_point)

        for index in range(self.leds):
            self[index + start_index] = colours[index]


class SingleIterator:
    """Iterate single indeces."""

    def __init__(self, eye, start_point="n", direction="clockwise"):
        """Construct."""
        self.eye = eye
        self.start_point = start_point
        self.direction = direction

        self.get_indeces()
        self.index = 0

    def get_indeces(self):
        """Work out our indeces."""
        points = FancyList(compass_points)
        points.rotate(steps=points.index(self.start_point))
        if self.direction == "clockwise":
            points.items = [points.items[0]] + list(reversed(points.items[1:]))  # noqa: RUF005

        self.indeces = [compass_points.index(item) for item in points.items]

    def __iter__(self):
        """Be in iterator."""
        return self

    def __next__(self):
        """Get `next`."""
        if self.index > len(self.indeces) - 1:
            raise StopIteration

        item = self.indeces[self.index]

        self.index += 1
        return item


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
