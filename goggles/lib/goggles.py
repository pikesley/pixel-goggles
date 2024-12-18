from lib.context import ring_size
from lib.eye import Eye
from lib.tools import is_single_colour


class Goggles:
    """An pair of giggles."""

    def __init__(self, pixels):
        """Construct."""
        self.pivels = pixels

        self.left = Eye(pixels, "left")
        self.right = Eye(pixels, "right")

    def load_ordering(self, point="n", rotation="anticlockwise", overlap=False):  # noqa: FBT002
        """Load the same ordering onto each eye."""
        for eye in [self.left, self.right]:
            eye.load_ordering(point=point, rotation=rotation, overlap=overlap)

    @property
    def ordering(self):
        """Full sequence, both eyes."""
        return self.left.ordering + self.right.ordering

    def fill(self, colours):
        """Fill the eyes."""
        if is_single_colour(colours):
            self.left.fill(colours)
            self.right.fill(colours)

        else:
            self.left.fill(colours[:ring_size])
            self.right.fill(colours[ring_size:])
