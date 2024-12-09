from lib.orderings import get_ordering, get_pairs, get_prime


def test_get_ordering():
    """Test we get orderings."""
    assert get_ordering("right", "n", "clockwise") == [
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
    assert get_ordering("right", "n", "anticlockwise") == [
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
    assert get_ordering("left", "n", "clockwise") == [
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
    assert get_ordering("left", "n", "clockwise") == [
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
    assert get_ordering("right", "e", "clockwise") == [
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
    assert get_ordering("left", "s", "clockwise") == [
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
    assert get_ordering("left", "nw", "clockwise") == [
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
        26,
        25,
    ]
    assert get_ordering("left", "nw", "clockwise", overlap=True) == [
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
        26,
        25,
        24,
    ]


def test_get_prime():
    """Test we can find the prime spot."""
    assert get_prime("right", "n") == 10  # noqa: PLR2004
    assert get_prime("left", "n") == 22  # noqa: PLR2004

    assert get_prime("right", "w") == 14  # noqa: PLR2004
    assert get_prime("left", "w") == 26  # noqa: PLR2004

    assert get_prime("right", "s") == 2  # noqa: PLR2004
    assert get_prime("left", "s") == 30  # noqa: PLR2004

    assert get_prime("right", "e") == 6  # noqa: PLR2004
    assert get_prime("left", "e") == 18  # noqa: PLR2004

    assert get_prime("right", "sw") == 0

    assert get_prime("left", "ese") == 17  # noqa: PLR2004


def test_get_pairs():
    """Test we get pairs."""
    assert get_pairs("right", "s") == [
        (2,),
        (1, 3),
        (0, 4),
        (15, 5),
        (14, 6),
        (13, 7),
        (12, 8),
        (11, 9),
        (10,),
    ]
