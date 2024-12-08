from lib.orderings import get_ordering, get_prime


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
    assert get_ordering("left", "north", "clockwise") == [
        22,
        21,
        20,
        19,
        18,
        17,
        16,
        31,
        30,
        29,
        28,
        27,
        26,
        25,
        24,
        23,
    ]
    assert get_ordering("left", "north", "clockwise") == [
        22,
        21,
        20,
        19,
        18,
        17,
        16,
        31,
        30,
        29,
        28,
        27,
        26,
        25,
        24,
        23,
    ]
    assert get_ordering("right", "east", "clockwise") == [
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
        10,
        9,
        8,
        7,
    ]
    assert get_ordering("left", "south", "clockwise") == [
        30,
        29,
        28,
        27,
        26,
        25,
        24,
        23,
        22,
        21,
        20,
        19,
        18,
        17,
        16,
        31,
    ]


def test_get_prime():
    """Test we can find the prime spot."""
    assert get_prime("right", "north") == 10  # noqa: PLR2004
    assert get_prime("left", "north") == 22  # noqa: PLR2004

    assert get_prime("right", "west") == 14  # noqa: PLR2004
    assert get_prime("left", "west") == 26  # noqa: PLR2004

    assert get_prime("right", "south") == 2  # noqa: PLR2004
    assert get_prime("left", "south") == 30  # noqa: PLR2004

    assert get_prime("right", "east") == 6  # noqa: PLR2004
    assert get_prime("left", "east") == 18  # noqa: PLR2004
