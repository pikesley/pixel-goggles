import os

patterns = []
if os.uname().sysname == "esp32":
    from patterns_list import patterns


class PatternManager:
    """Manage patterns."""

    def __init__(self, patterns_list=patterns):
        """Construct."""
        self.patterns_list = patterns_list
        self.names = [item.__name__ for item in self.patterns_list]

    def index_by_name(self, name):
        """Get the index for an entry by its name."""
        try:
            return self.names.index(name)
        except ValueError:
            return 0
