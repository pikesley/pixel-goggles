from math import isclose

from lib.tools import get_intervals, inverse_square_tail, pendulum_timings


def test_inverse_square_tail():
    """Test the tail."""
    assert list(inverse_square_tail(8)) == [
        1.0,
        0.5,
        0.25,
        0.125,
        0.0625,
        0.03125,
        0.015625,
        0.0078125,
    ]
    assert list(inverse_square_tail(4, backwards=True)) == [0.125, 0.25, 0.5, 1.0]
    assert list(inverse_square_tail(3)) == [1.0, 0.5, 0.25]

    assert list(inverse_square_tail(8, coefficient=0.5)) == [
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
    assert list(get_intervals(100000)) == [
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


def test_pendulum_timings():
    """Test the pendulum timings."""
    expected = [
        0.9951847266721968,
        0.9569403357322089,
        0.881921264348355,
        0.7730104533627371,
        0.6343932841636455,
        0.47139673682599786,
        0.2902846772544624,
        0.09801714032956083,
        0.09801714032956083,
        0.2902846772544624,
        0.47139673682599786,
        0.6343932841636455,
        0.7730104533627371,
        0.881921264348355,
        0.9569403357322089,
        0.9951847266721968,
    ]
    actual = pendulum_timings()

    for i in range(len(actual)):
        assert isclose(actual[i], expected[i])
