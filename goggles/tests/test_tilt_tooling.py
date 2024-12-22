from lib.tilt_tooling import (
    assign_ranges,
    filled_points,
    locate_points,
    rotation_lookups,
)


def test_easy_filling():
    """Test the easy case."""
    assert filled_points("n", 1.0) == [
        "n",
        "nnw",
        "nw",
        "wnw",
        "w",
        "wsw",
        "sw",
        "ssw",
        "s",
        "sse",
        "se",
        "ese",
        "e",
        "ene",
        "ne",
        "nne",
    ]


def test_flat_filling():
    """Test for 50% full."""
    assert filled_points("n", 0.5) == (
        ["w", "wsw", "sw", "ssw", "s", "sse", "se", "ese", "e"]
    )


def test_tilted_filling():
    """Test when it's rotated."""
    assert filled_points("nne", 0.3) == (["sw", "ssw", "s"])


def test_locating_points():
    """Test it pairs up the points."""
    assert locate_points("n") == {
        "n": 1.0,
        "nnw": 0.8086582838174551,
        "nw": 0.6464466094067263,
        "wnw": 0.5380602337443566,
        "w": 0.5,
        "wsw": 0.46193976625564337,
        "sw": 0.3535533905932738,
        "ssw": 0.19134171618254492,
        "s": 0,
        "sse": 0.19134171618254492,
        "se": 0.3535533905932738,
        "ese": 0.46193976625564337,
        "e": 0.5,
        "ene": 0.5380602337443566,
        "ne": 0.6464466094067263,
        "nne": 0.8086582838174551,
    }

    assert locate_points("wnw") == {
        "wnw": 1.0,
        "w": 0.8086582838174551,
        "wsw": 0.6464466094067263,
        "sw": 0.5380602337443566,
        "ssw": 0.5,
        "s": 0.46193976625564337,
        "sse": 0.3535533905932738,
        "se": 0.19134171618254492,
        "ese": 0,
        "e": 0.19134171618254492,
        "ene": 0.3535533905932738,
        "ne": 0.46193976625564337,
        "nne": 0.5,
        "n": 0.5380602337443566,
        "nnw": 0.6464466094067263,
        "nw": 0.8086582838174551,
    }


def test_assign_ranges():
    """Test it assigns ranges correctly."""
    assert assign_ranges(-4, 4) == {
        "w": (-4.5, -3.5),
        "wnw": (-3.5, -2.5),
        "nw": (-2.5, -1.5),
        "nnw": (-1.5, -0.5),
        "n": (-0.5, 0.5),
        "nne": (0.5, 1.5),
        "ne": (1.5, 2.5),
        "ene": (2.5, 3.5),
        "e": (3.5, 4.5),
    }

    assert assign_ranges(-8, 8) == {
        "w": (-9, -7),
        "wnw": (-7, -5),
        "nw": (-5, -3),
        "nnw": (-3, -1),
        "n": (-1, 1),
        "nne": (1, 3),
        "ne": (3, 5),
        "ene": (5, 7),
        "e": (7, 9),
    }


def test_off_balance_ranges():
    """Test it compensates for an unbalanced range."""
    assert assign_ranges(-3, 5) == {
        "w": (-3.5, -2.5),
        "wnw": (-2.5, -1.5),
        "nw": (-1.5, -0.5),
        "nnw": (-0.5, 0.5),
        "n": (0.5, 1.5),
        "nne": (1.5, 2.5),
        "ne": (2.5, 3.5),
        "ene": (3.5, 4.5),
        "e": (4.5, 5.5),
    }

    assert assign_ranges(-5, 3) == {
        "w": (-5.5, -4.5),
        "wnw": (-4.5, -3.5),
        "nw": (-3.5, -2.5),
        "nnw": (-2.5, -1.5),
        "n": (-1.5, -0.5),
        "nne": (-0.5, 0.5),
        "ne": (0.5, 1.5),
        "ene": (1.5, 2.5),
        "e": (2.5, 3.5),
    }

    assert assign_ranges(0, 8) == {
        "w": (-0.5, 0.5),
        "wnw": (0.5, 1.5),
        "nw": (1.5, 2.5),
        "nnw": (2.5, 3.5),
        "n": (3.5, 4.5),
        "nne": (4.5, 5.5),
        "ne": (5.5, 6.5),
        "ene": (6.5, 7.5),
        "e": (7.5, 8.5),
    }


def test_rotation_lookups():
    """Test the lookups."""
    assert rotation_lookups(-4, 4) == {
        -4: "w",
        -3: "wnw",
        -2: "nw",
        -1: "nnw",
        0: "n",
        1: "nne",
        2: "ne",
        3: "ene",
        4: "e",
    }

    assert rotation_lookups(-8, 8) == {
        -8: "w",
        -7: "w",
        -6: "wnw",
        -5: "wnw",
        -4: "nw",
        -3: "nw",
        -2: "nnw",
        -1: "nnw",
        0: "n",
        1: "n",
        2: "nne",
        3: "nne",
        4: "ne",
        5: "ne",
        6: "ene",
        7: "ene",
        8: "e",
    }
