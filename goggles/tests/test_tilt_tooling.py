from lib.tilt_tooling import filled_points, locate_points


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
