from hashlib import md5
from pathlib import Path

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

    assert list(left_antis["n"]) == (
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 1]
    )
    assert list(left_antis["nnw"]) == (
        [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2]
    )
    assert list(left_antis["nw"]) == (
        [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3]
    )
    assert list(left_antis["w"]) == (
        [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5]
    )


def test_make_left_clockwise():
    """Test it reverses the easy side."""
    left_clocks = make_left_clockwise()

    assert list(left_clocks["n"]) == (
        [2, 1, 0, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3]
    )
    assert list(left_clocks["nnw"]) == (
        [3, 2, 1, 0, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4]
    )
    assert list(left_clocks["nw"]) == (
        [4, 3, 2, 1, 0, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]
    )
    assert list(left_clocks["w"]) == (
        [6, 5, 4, 3, 2, 1, 0, 15, 14, 13, 12, 11, 10, 9, 8, 7]
    )


def test_make_right_anticlockwise():
    """Test it does the right side."""
    right_antis = make_right_anticlockwise()

    assert list(right_antis["n"]) == (
        [30, 31, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
    )
    assert list(right_antis["s"]) == (
        [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 16, 17, 18, 19, 20, 21]
    )
    assert list(right_antis["e"]) == (
        [26, 27, 28, 29, 30, 31, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    )


def test_make_right_clockwise():
    """Test it does the right side."""
    right_clocks = make_right_clockwise()

    assert list(right_clocks["n"]) == (
        [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 31]
    )
    assert list(right_clocks["s"]) == (
        [22, 21, 20, 19, 18, 17, 16, 31, 30, 29, 28, 27, 26, 25, 24, 23]
    )
    assert list(right_clocks["e"]) == (
        [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 31, 30, 29, 28, 27]
    )


def test_make_pairs():
    """Test it makes pairs."""
    left_pairs = make_left_pairs()
    assert list(left_pairs["n"]) == (
        [(2,), (1, 3), (0, 4), (5, 15), (6, 14), (7, 13), (8, 12), (9, 11), (10,)]
    )

    right_pairs = make_right_pairs()
    assert list(right_pairs["s"]) == (
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


def test_file_hashes():
    """Test it made the same files."""
    target = Path("renders", "eyes").glob("**/*")
    hashes = []

    for item in target:
        if item.is_file():
            m = md5()  # noqa: S324
            m.update(item.read_bytes())
            hashes.append(m.hexdigest())

    hashes.sort()
    total_hash = md5()  # noqa: S324
    total_hash.update("\n".join(hashes).encode())

    assert total_hash.hexdigest() == "0c515ec77897c3c53c7016f3d153aebf"
