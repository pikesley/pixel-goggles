class FakePixels(list):
    """Fake NeoPixels for testing."""

    def __init__(self, length=32):
        """Construct."""
        self.length = length
        for _ in range(self.length):
            self.append((0, 0, 0))
