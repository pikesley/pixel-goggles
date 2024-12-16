import json


class Eye:
    """One eye of a goggle."""

    def __init__(self, pixels, side, leds=16):
        """Construct."""
        self.pixels = pixels
        self.side = side
        self.leds = leds

        self.offset = 0
        if self.side == "right":
            self.offset = self.leds

        self.load_ordering("n", "anticlockwise")

    # TODO: set prime_point or something?
    # How do we handle pairs?
    def load_ordering(self, point="n", rotation="anticlockwise"):
        """Set our ordering."""
        self.ordering = json.load(
            open(f"renders/eyes/{self.side}/{point}/{rotation}.json")  # noqa: SIM115, PTH123
        )

    def __setitem__(self, index, colour):
        """Colour a pixel."""
        self.pixels[index] = colour

    def __getitem__(self, index):
        """Get an item."""
        return self.pixels[index]

    def fill(self, colours):
        """Fill ourself with a list of colours."""
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
