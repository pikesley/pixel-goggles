from lib.eye import Eye


class Goggles:
    """An pair of giggles."""

    def __init__(self, pixels):
        """Construct."""
        self.pivels = pixels

        self.left = Eye(pixels, "left")
        self.right = Eye(pixels, "right")

    def load_ordering(self, point="n", rotation="anticlockwise", overlap=False):  # noqa: FBT002
        """Load orderings onto our eyes."""
        for eye in [self.left, self.right]:
            eye.load_ordering(point=point, rotation=rotation, overlap=overlap)
        # self.left.load_ordering(point=point, rotation=rotation, overlap=overlap)
        # self.right.load_ordering(point=point, rotation=rotation, overlap=overlap)

    @property
    def ordering(self):
        """Full sequence, both eyes."""
        return self.left.ordering + self.right.ordering

    # TODO: this doesn't really work, should split sequence
    def fill(self, colours):
        """Fill the eyes."""
        for eye in [self.left, self.right]:
            eye.fill(colours)
