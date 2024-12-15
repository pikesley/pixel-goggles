from helpers.fake_pixels import FakePixels

from lib.eye import Eye


def test_remapping():
    """Test it remaps indeces."""
    pixels = FakePixels()
    left_eye = Eye(pixels, "left")

    left_eye[0] = (255, 0, 0)
    assert pixels[2] == (255, 0, 0)

    right_eye = Eye(pixels, "right")

    right_eye[0] = (0, 0, 255)
    assert pixels[30] == (0, 0, 255)


def test_colour_point():
    """Test it colours a point."""
    pixels = FakePixels()
    eye = Eye(pixels, "right")

    eye.colour_point("s", (255, 0, 0))
    assert pixels[22] == (255, 0, 0)


def test_fill():
    """Test it fills."""
    pixels = FakePixels()

    left_eye = Eye(pixels, "left")
    left_eye.fill("n", list(range(0, 16, 1)))

    right_eye = Eye(pixels, "right")
    right_eye.fill("n", list(range(100, 116, 1)))

    assert pixels == [
        14,
        15,
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        102,
        103,
        104,
        105,
        106,
        107,
        108,
        109,
        110,
        111,
        112,
        113,
        114,
        115,
        100,
        101,
    ]
