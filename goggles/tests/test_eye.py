from lib.eye import Eye
from tests.helpers.fake_pixels import FakePixels


def test_single_filling():
    """Test filling from single ordering."""
    pixels = FakePixels(16)
    eye = Eye(pixels, "left")
    eye.load_ordering()
    colours = list(range(100, 116))

    eye.fill(colours)
    assert pixels == (
        [114, 115, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]
    )


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


# def test_remapping():
#     """Test it remaps indeces."""
#     pixels = FakePixels()
#     left_eye = Eye(pixels, "left")

#     left_eye[0] = (255, 0, 0)
#     assert pixels[2] == (255, 0, 0)

#     right_eye = Eye(pixels, "right")

#     right_eye[0] = (0, 0, 255)
#     assert pixels[30] == (0, 0, 255)


def test_colour_point():
    """Test it colours a point."""
    pixels = FakePixels(32)
    eye = Eye(pixels, "right")

    eye.colour_point("s", (255, 0, 0))
    assert pixels[22] == (255, 0, 0)

    eye.colour_point("nw", (0, 255, 0))
    assert pixels[16] == (0, 255, 0)

    print("THIS WORKS BY ACCIDENT!!!")
