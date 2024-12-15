from lib.eye import Eye, FakePixels


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
