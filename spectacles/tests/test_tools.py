from lib.tools import inverse_square_tail, rotate_list


def test_rotate_list():
    """Test we can rotate."""
    example = [5, 3, 7, 8, 1, 10]

    assert rotate_list(example) == [3, 7, 8, 1, 10, 5]
    assert rotate_list(example, direction="r") == [10, 5, 3, 7, 8, 1]
    assert rotate_list(example, steps=2) == [7, 8, 1, 10, 5, 3]


def test_inverse_square_tail():
    """Test the tail."""
    assert inverse_square_tail(8) == [
        1.0,
        0.5,
        0.25,
        0.125,
        0.0625,
        0.03125,
        0.015625,
        0.0078125,
    ]
    assert inverse_square_tail(4, backwards=True) == [0.125, 0.25, 0.5, 1.0]
    assert inverse_square_tail(3) == [1.0, 0.5, 0.25]

    assert inverse_square_tail(8, coefficient=0.5) == [
        1.0,
        0.7071067811865475,
        0.5,
        0.35355339059327373,
        0.25,
        0.17677669529663687,
        0.125,
        0.08838834764831843,
    ]
