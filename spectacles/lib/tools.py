def index_pairs(length, offset):
    """Calculate index-pairs."""
    return [
        (_first_index(index, offset, length), _second_index(index, offset, length))
        for index in range(int(length / 2))
    ]


def _first_index(index, offset, length):
    """Get the first half of a pair."""
    return (offset + index) % length


def _second_index(index, offset, length):
    """Get the second half of a pair."""
    return (offset - length - index - 1) % length