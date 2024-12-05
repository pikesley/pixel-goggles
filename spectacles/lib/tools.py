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


def clockwise_index(index, offset, length):
    """Get an index for rotating clockwise."""
    return (index + offset) % length


def anti_clockwise_index(index, offset, length):
    """Get an index for rotating anti-clockwise."""
    return length - 1 - ((index + offset) % length)
