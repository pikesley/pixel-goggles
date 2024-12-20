class Wings:
    """Wave about."""

    # TODO: maybe a full circle?
    def __init__(self):
        """Construct."""
        self.patterns = ["nx", "xnx", "x", "xsx", "sx"]
        self.patterns += list(reversed(self.patterns[1:-1]))
        self.index = 0

    def __iter__(self):
        """Be an iterator."""
        return self

    def __next__(self):
        """Iterate."""
        if self.index > len(self.patterns) - 1:
            self.index = self.index % len(self.patterns)

        item = {
            "left": self.patterns[self.index].replace("x", "w"),
            "right": self.patterns[self.index].replace("x", "e"),
        }
        self.index += 1

        return item
