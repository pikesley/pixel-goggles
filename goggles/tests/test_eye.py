from lib.eye import Eye
from tests.helpers.fake_pixels import FakePixels


def test_single_filling():
    """Test filling from single ordering."""
    pixels = FakePixels(16)
    eye = Eye(pixels, "left")
    eye.load_ordering(point="n")
    colours = list(range(100, 116))

    eye.fill(colours)
    assert pixels == (
        [114, 115, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]
    )


def test_single_filling_with_different_prime():
    """Test filling from single ordering with a non-north origin."""
    pixels = FakePixels(16)
    eye = Eye(pixels, "left")
    eye.load_ordering(point="s")
    colours = list(range(100, 116))

    eye.fill(colours)
    assert pixels == (
        [106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 100, 101, 102, 103, 104, 105]
    )


def test_point_colouring():
    """Test it knows where its points are."""
    pixels = FakePixels(16, default=0)
    eye = Eye(pixels, "left")
    eye.load_ordering(point="n")

    eye["n"] = 1
    assert pixels == ([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


def test_trickier_point_colouring():
    """Test it knows where its points are, from a different direction."""
    pixels = FakePixels(16, default=0)
    eye = Eye(pixels, "left")
    eye.load_ordering(point="s")

    eye["n"] = 1
    assert pixels == ([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


def test_even_trickier_point_colouring():
    """Test it knows where its points are, from another different direction."""
    pixels = FakePixels(16, default=0)
    eye = Eye(pixels, "left")
    eye.load_ordering(point="wsw")

    eye["n"] = 1
    assert pixels == ([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


def test_pair_filling():
    """Test filling from pairwise ordering."""
    pixels = FakePixels(16)
    eye = Eye(pixels, "left")
    eye.load_ordering(rotation="pairs", point="ne")
    colours = list(range(100, 109))

    eye.fill(colours)
    assert pixels == (
        [100, 101, 102, 103, 104, 105, 106, 107, 108, 107, 106, 105, 104, 103, 102, 101]
    )


def test_right_side_filling():
    """Test filling the right eye."""
    pixels = FakePixels(32)
    eye = Eye(pixels, "right")
    eye.load_ordering(point="s")
    colours = list(range(200, 220))

    eye.fill(colours)
    assert pixels[16:] == (
        [210, 211, 212, 213, 214, 215, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209]
    )


def test_indexing_on_pairs():
    """Test it can handle an index when it has pairs."""
    pixels = FakePixels(16, default=0)
    eye = Eye(pixels, "left")
    eye.load_ordering(rotation="pairs", point="n")

    for i in range(9):
        eye.set_pair(i, i)

    assert pixels == ([2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3])
