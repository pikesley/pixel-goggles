from helpers.fake_pixels import FakePixels

from lib.eye import Eye


def test_constructor():
    """Test it gets the data."""
    pixels = FakePixels()
    eye = Eye(pixels, "left", 2)

    assert eye.compass == {
        "n": 2,
        "nnw": 3,
        "nw": 4,
        "wnw": 5,
        "w": 6,
        "wsw": 7,
        "sw": 8,
        "ssw": 9,
        "s": 10,
        "sse": 11,
        "se": 12,
        "ese": 13,
        "e": 14,
        "ene": 15,
        "ne": 0,
        "nne": 1,
    }


def test_right_eye():
    """Test it constructs with an offset."""
    pixels = FakePixels()
    eye = Eye(pixels, "right", 30)

    assert eye.compass == {
        "n": 30,
        "nnw": 31,
        "nw": 16,
        "wnw": 17,
        "w": 18,
        "wsw": 19,
        "sw": 20,
        "ssw": 21,
        "s": 22,
        "sse": 23,
        "se": 24,
        "ese": 25,
        "e": 26,
        "ene": 27,
        "ne": 28,
        "nne": 29,
    }


def test_remapping():
    """Test it remaps indeces."""
    pixels = FakePixels()
    eye = Eye(pixels, "left", 2)

    eye[0] = (255, 0, 0)
    assert eye.pixels[2] == (255, 0, 0)
