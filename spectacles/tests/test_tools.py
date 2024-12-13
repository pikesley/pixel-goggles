from lib.tools import get_intervals, inverse_square_tail


def test_inverse_square_tail():
    """Test the tail."""
    assert inverse_square_tail(8).items == [
        1.0,
        0.5,
        0.25,
        0.125,
        0.0625,
        0.03125,
        0.015625,
        0.0078125,
    ]
    assert inverse_square_tail(4, backwards=True).items == [0.125, 0.25, 0.5, 1.0]
    assert inverse_square_tail(3).items == [1.0, 0.5, 0.25]

    assert inverse_square_tail(8, coefficient=0.5).items == [
        1.0,
        0.7071067811865475,
        0.5,
        0.35355339059327373,
        0.25,
        0.17677669529663687,
        0.125,
        0.08838834764831843,
    ]


def test_get_intervals():
    """Test intervals."""
    assert get_intervals(100000).items == [
        7612,
        21677,
        32442,
        38268,
        38268,
        32442,
        21677,
        7612,
        0,
    ]
