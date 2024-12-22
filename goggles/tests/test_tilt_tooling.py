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
    assert filled_points("e", 0.5) == (
        ["n", "nnw", "nw", "wnw", "w", "wsw", "sw", "ssw", "s"]
    )
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
        "w": (4.5, 3.5),
        "wnw": (3.5, 2.5),
        "nw": (2.5, 1.5),
        "nnw": (1.5, 0.5),
        "n": (0.5, -0.5),
        "nne": (-0.5, -1.5),
        "ne": (-1.5, -2.5),
        "ene": (-2.5, -3.5),
        "e": (-3.5, -4.5),
    }

    assert assign_ranges(-8, 8) == {
        "w": (9.0, 7.0),
        "wnw": (7.0, 5.0),
        "nw": (5.0, 3.0),
        "nnw": (3.0, 1.0),
        "n": (1.0, -1.0),
        "nne": (-1.0, -3.0),
        "ne": (-3.0, -5.0),
        "ene": (-5.0, -7.0),
        "e": (-7.0, -9.0),
    }


def test_off_balance_ranges():
    """Test it compensates for an unbalanced range."""
    assert assign_ranges(-3, 5) == {
        "w": (5.5, 4.5),
        "wnw": (4.5, 3.5),
        "nw": (3.5, 2.5),
        "nnw": (2.5, 1.5),
        "n": (1.5, 0.5),
        "nne": (0.5, -0.5),
        "ne": (-0.5, -1.5),
        "ene": (-1.5, -2.5),
        "e": (-2.5, -3.5),
    }
    assert assign_ranges(-5, 3) == {
        "w": (3.5, 2.5),
        "wnw": (2.5, 1.5),
        "nw": (1.5, 0.5),
        "nnw": (0.5, -0.5),
        "n": (-0.5, -1.5),
        "nne": (-1.5, -2.5),
        "ne": (-2.5, -3.5),
        "ene": (-3.5, -4.5),
        "e": (-4.5, -5.5),
    }
    assert assign_ranges(0, 8) == {
        "w": (8.5, 7.5),
        "wnw": (7.5, 6.5),
        "nw": (6.5, 5.5),
        "nnw": (5.5, 4.5),
        "n": (4.5, 3.5),
        "nne": (3.5, 2.5),
        "ne": (2.5, 1.5),
        "ene": (1.5, 0.5),
        "e": (0.5, -0.5),
    }


def test_rotation_lookups():
    """Test the lookups."""
    assert rotation_lookups(-4, 4) == {
        -4: "e",
        -3: "ene",
        -2: "ne",
        -1: "nne",
        0: "n",
        1: "nnw",
        2: "nw",
        3: "wnw",
        4: "w",
    }
    assert rotation_lookups(-8, 8) == {
        -8: "e",
        -7: "e",
        -6: "ene",
        -5: "ene",
        -4: "ne",
        -3: "ne",
        -2: "nne",
        -1: "nne",
        0: "n",
        1: "n",
        2: "nnw",
        3: "nnw",
        4: "nw",
        5: "nw",
        6: "wnw",
        7: "wnw",
        8: "w",
    }
