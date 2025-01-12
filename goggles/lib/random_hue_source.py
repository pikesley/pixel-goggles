from random import random


class RandomHueSource:
    """Generate spaced-out random hues."""

    def __init__(self, distance=0.3):
        """Construct."""
        self.distance = distance
        self.current_hue = self.next_hue = random()  # noqa: S311

    def hue(self):
        """Get a hue."""
        while abs(self.current_hue - self.next_hue) < self.distance:
            self.next_hue = random()  # noqa: S311

        self.current_hue = self.next_hue

        return self.current_hue
