import json

from lib.compass_points import compass_points, tops
from lib.context import ring_size
from lib.tools import is_single_colour


class Eye:
    """One eye of a goggle."""

    def __init__(self, pixels, side):
        """Construct."""
        self.pixels = pixels
        self.side = side
        self.north_index = tops[self.side]
        self.prime_point = "n"
        self.load_ordering(self.prime_point, "anticlockwise")

    def load_ordering(self, point="n", rotation="anticlockwise", overlap=False):  # noqa: FBT002
        """Set our ordering."""
        self.prime_point = point
        self.ordering = json.load(
            open(f"renders/eyes/{self.side}/{point}/{rotation}.json")  # noqa: SIM115, PTH123
        )
        if overlap:
            self.ordering = self.ordering + [self.ordering[0]]  # noqa: RUF005

    def __setitem__(self, index, colour):
        """Colour a pixel."""
        if isinstance(index, str):
            index = compass_points.index(index) - compass_points.index(self.prime_point)

        self.pixels[self.ordering[index]] = colour

    def __getitem__(self, index):
        """Get an item."""
        return self.ordering[index]

    def set_pair(self, index, colour):
        """Set some items."""
        for item in self.ordering[index]:
            self.pixels[item] = colour

    def fill(self, colours):
        """Fill ourself with a single colour, or list of colours."""
        if is_single_colour(colours):
            colours = [colours] * ring_size

        for index, item in enumerate(self.ordering):
            if isinstance(item, list):
                for subitem in item:
                    self.pixels[subitem] = colours[index]

            else:
                self.pixels[item] = colours[index]

    def __iter__(self):
        """Be an iterator."""
        self.count = 0
        return self

    def __next__(self):
        """Return our indeces."""
        if self.count >= len(self.ordering):
            raise StopIteration

        item = self.ordering[self.count]
        self.count += 1
        return item
