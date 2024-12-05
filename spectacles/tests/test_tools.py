from lib.tools import index_pairs, rotation_index


def test_index_pairs():
    """Test index_pairs."""
    assert index_pairs(12, 0) == [
        (0, 11),
        (1, 10),
        (2, 9),
        (3, 8),
        (4, 7),
        (5, 6),
    ]

    assert index_pairs(12, 4) == [
        (4, 3),
        (5, 2),
        (6, 1),
        (7, 0),
        (8, 11),
        (9, 10),
    ]


def test_clockwise_index():
    """Test clockwise index."""
    assert rotation_index(0, 0, 12) == 0
    assert rotation_index(1, 3, 12) == 4  # noqa: PLR2004
    assert rotation_index(10, 3, 12) == 1


def test_anti_clockwise_index():
    """Test anti-clockwise index."""
    assert rotation_index(0, 0, 12, direction="anti-clockwise") == 11  # noqa: PLR2004
    assert rotation_index(1, 0, 12, direction="anti-clockwise") == 10  # noqa: PLR2004
    assert rotation_index(2, 0, 12, direction="anti-clockwise") == 9  # noqa: PLR2004

    assert rotation_index(5, 8, 12, direction="anticlockwise") == 10  # noqa: PLR2004
