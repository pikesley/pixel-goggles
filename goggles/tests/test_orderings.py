from lib.orderings import get_ordering, get_pairs, get_prime


def test_get_ordering():
    """Test we get orderings."""
    assert get_ordering("right", "n", "clockwise") == [
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
    assert get_ordering("right", "n", "anticlockwise") == [
        30,
        31,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
    ]
    assert get_ordering("left", "n", "clockwise") == [
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
        6,
        5,
        4,
        3,
    ]
    assert get_ordering("right", "e", "clockwise") == [
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
        30,
        29,
        28,
        27,
    ]
    assert get_ordering("left", "s", "clockwise") == [
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
    assert get_ordering("left", "nw", "clockwise") == [
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
        6,
        5,
    ]
    assert get_ordering("left", "nw", "clockwise", overlap=True) == [
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
        6,
        5,
        4,
    ]


def test_get_prime():
    """Test we can find the prime spot."""
    assert get_prime("right", "n") == 30  # noqa: PLR2004
    assert get_prime("left", "n") == 2  # noqa: PLR2004

    assert get_prime("right", "w") == 18  # noqa: PLR2004
    assert get_prime("left", "w") == 6  # noqa: PLR2004

    assert get_prime("right", "s") == 22  # noqa: PLR2004
    assert get_prime("left", "s") == 10  # noqa: PLR2004

    assert get_prime("right", "e") == 26  # noqa: PLR2004
    assert get_prime("left", "e") == 14  # noqa: PLR2004

    assert get_prime("right", "sw") == 20  # noqa: PLR2004

    assert get_prime("left", "ese") == 13  # noqa: PLR2004


def test_get_pairs():
    """Test we get pairs."""
    assert get_pairs("right", "s") == [
        (22,),
        (21, 23),
        (20, 24),
        (19, 25),
        (18, 26),
        (17, 27),
        (16, 28),
        (31, 29),
        (30,),
    ]
