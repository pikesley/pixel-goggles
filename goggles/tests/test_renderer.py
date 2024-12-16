from renderer import (
    make_left_anticlockwise,
    make_left_clockwise,
    make_left_pairs,
    make_right_anticlockwise,
    make_right_clockwise,
    make_right_pairs,
)


def test_make_left_anticlockwise():
    """Test it makes the easy side."""
    left_antis = make_left_anticlockwise()

    assert left_antis["n"].items == (
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 1]
    )
    assert left_antis["nnw"].items == (
        [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2]
    )
    assert left_antis["nw"].items == (
        [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3]
    )
    assert left_antis["w"].items == (
        [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5]
    )


def test_make_left_clockwise():
    """Test it reverses the easy side."""
    left_clocks = make_left_clockwise()

    assert left_clocks["n"].items == (
        [2, 1, 0, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3]
    )
    assert left_clocks["nnw"].items == (
        [3, 2, 1, 0, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4]
    )
    assert left_clocks["nw"].items == (
        [4, 3, 2, 1, 0, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]
    )
    assert left_clocks["w"].items == (
        [6, 5, 4, 3, 2, 1, 0, 15, 14, 13, 12, 11, 10, 9, 8, 7]
    )


def test_make_right_anticlockwise():
    """Test it does the right side."""
    right_antis = make_right_anticlockwise()

    assert right_antis["n"].items == (
        [30, 31, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
    )
    assert right_antis["s"].items == (
        [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 16, 17, 18, 19, 20, 21]
    )
    assert right_antis["e"].items == (
        [26, 27, 28, 29, 30, 31, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    )


def test_make_right_clockwise():
    """Test it does the right side."""
    right_clocks = make_right_clockwise()

    assert right_clocks["n"].items == (
        [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 31]
    )
    assert right_clocks["s"].items == (
        [22, 21, 20, 19, 18, 17, 16, 31, 30, 29, 28, 27, 26, 25, 24, 23]
    )
    assert right_clocks["e"].items == (
        [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 31, 30, 29, 28, 27]
    )


def test_make_pairs():
    """Test it makes pairs."""
    left_pairs = make_left_pairs()
    assert left_pairs["n"].items == (
        [(2,), (1, 3), (0, 4), (5, 15), (6, 14), (7, 13), (8, 12), (9, 11), (10,)]
    )

    right_pairs = make_right_pairs()
    assert right_pairs["s"].items == (
        [
            (22,),
            (21, 23),
            (20, 24),
            (19, 25),
            (18, 26),
            (17, 27),
            (16, 28),
            (29, 31),
            (30,),
        ]
    )
