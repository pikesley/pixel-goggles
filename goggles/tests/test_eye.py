from helpers.fake_pixels import FakePixels

from lib.eye import Eye


def test_remapping():
    """Test it remaps indeces."""
    pixels = FakePixels()
    eye = Eye(pixels, "left", 2)

    eye[0] = (255, 0, 0)
    assert eye.pixels[2] == (255, 0, 0)


def test_colour_point():
    """Test it colours a point."""
    pixels = FakePixels()
    eye = Eye(pixels, "right", 30)

    eye.colour_point("n", (255, 0, 0))
    assert eye.pixels[0] == (255, 0, 0)
