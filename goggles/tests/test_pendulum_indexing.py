from lib.pendulum_indexing import pendulum_timings, sequence


def test_timings():
    """Test timings."""
    assert pendulum_timings() == [
        0.9951847266721968,
        0.9569403357322089,
        0.8819212643483549,
        0.773010453362737,
        0.6343932841636455,
        0.47139673682599764,
        0.29028467725446233,
        0.0980171403295606,
        0.0980171403295606,
        0.29028467725446233,
        0.47139673682599764,
        0.6343932841636455,
        0.773010453362737,
        0.8819212643483549,
        0.9569403357322089,
        0.9951847266721968,
    ]


def test_limited_timings():
    """Test truncated timings."""
    assert pendulum_timings(length=2) == [
        0.0980171403295606,
        0.0980171403295606,
    ]

    assert pendulum_timings(length=4) == [
        0.29028467725446233,
        0.0980171403295606,
        0.0980171403295606,
        0.29028467725446233,
    ]


def test_short_sequence():
    """Test a short sequence."""
    assert sequence(1) == {
        "indeces": [7, 8, 9],
        "points": ["ssw", "s", "sse"],
        "intervals": [
            0.0980171403295606,
            0.0980171403295606,
        ],
    }


def test_longer_sequence():
    """Test a longer sequence."""
    assert sequence(3) == {
        "indeces": [5, 6, 7, 8, 9, 10, 11],
        "points": ["wsw", "sw", "ssw", "s", "sse", "se", "ese"],
        "intervals": [
            0.47139673682599764,
            0.29028467725446233,
            0.0980171403295606,
            0.0980171403295606,
            0.29028467725446233,
            0.47139673682599764,
        ],
    }
