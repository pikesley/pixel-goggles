class FancyList:
    """List with extra steps."""

    def __init__(self, items, circular=False):  # noqa: FBT002
        """Construct."""
        self.items = self.default_items = items
        self.circular = circular

    def __getitem__(self, index):
        """`[index]`."""
        if self.circular and index > len(self) - 1:
            index = index % len(self)
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

    def trim(self, end="front"):
        """Trim an item."""
        if end == "front":
            self.items = self.items[1:]

        else:
            self.items = self.items[:-1]

    def empty(self):
        """Are we out of items."""
        return self.items == []

    def index(self, item):
        """Get the index of `item`."""
        return self.items.index(item)

    def reverse(self):
        """`reverse()`."""
        self.items.reverse()

    def update(self, contents):
        """Update our `items`."""
        self.items = contents

    def reset(self):
        """Back to initial state."""
        self.items = self.default_items
