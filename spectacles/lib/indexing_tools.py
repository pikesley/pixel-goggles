def index_pairs(length, offset):
    """Calculate index-pairs."""
    return [
        tuple(
            [method(index, offset, length) for method in (_first_index, _second_index)]
        )
        for index in range(int(length / 2))
    ]


def _first_index(index, offset, length):
    """Get the first half of a pair."""
    return (offset + index) % length


def _second_index(index, offset, length):
    """Get the second half of a pair."""
    return (offset - length - index - 1) % length


def rotation_index(index, offset, length, direction="clockwise"):
    """Get a rotation index."""
    rot_index = (index + offset) % length

    if "anti" not in direction:
        rot_index = length - rot_index - 1

    return rot_index


def intensity_list(length):
    """Get a scaled list of brightnesses."""
    return [((i + 1) * 1 / length) for i in range(length - 1, -1, -1)]