class RotatableList:
    """Rotatable list."""

    def __init__(self, items):
        """Construct."""
        self.items = items

    def __getitem__(self, index):
        """`[index]`."""
        return self.items[index]

    def __len__(self):
        """`len()`."""
        return len(self.items)

    def append(self, item):
        """`append(foo)`."""
        self.items.append(item)

    @property
    def head(self):
        """Get our first item."""
        return self.items[0]

    def rotate(self, direction="l", steps=1):
        """Rotate ourself."""
        if direction == "l":
            for _ in range(steps):
                self.items = self.items[1:] + [self.items[0]]

        else:
            for _ in range(steps):
                self.items = [self.items[-1]] + self.items[:-1]