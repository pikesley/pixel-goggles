from lib.orderings import get_ordering


def test_get_ordering():
    """Test we get orderings."""
    assert get_ordering("right", "north", "clockwise") == [
        10,
        9,
        8,
        7,
        6,
        5,
        4,
        3,
        2,
        1,
        0,
        15,
        14,
        13,
        12,
        11,
    ]
    assert get_ordering("right", "north", "anticlockwise") == [
        10,
        11,
        12,
        13,
        14,
        15,
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
    ]

    # assert get_ordering("left", "north", "clockwise")
