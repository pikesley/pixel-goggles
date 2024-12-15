from helpers.fake_pixels import FakePixels

from lib.eye import Eye, PairwiseIterator, SingleIterator


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
    left_eye.fill(list(range(0, 16, 1)))

    right_eye = Eye(pixels, "right")
    right_eye.fill(list(range(100, 116, 1)), "n")

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


def test_iterator():
    """Test the iterator."""
    pixels = FakePixels()
    eye = Eye(pixels, "left")

    iterator = SingleIterator(eye, "e")
    assert iterator.indeces == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 15, 14, 13]

    iterator = SingleIterator(eye, "w")
    assert iterator.indeces == [4, 3, 2, 1, 0, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]

    iterator = SingleIterator(eye, "n", "anticlockwise")
    assert iterator.indeces == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    results = []
    for _ in range(16):
        results.append(next(iterator))  # noqa: PERF401

    assert results == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def test_pairwise_iterator():
    """Test the pairwise-iterator."""
    pixels = FakePixels()
    eye = Eye(pixels, "left")

    iterator = PairwiseIterator(eye, "n")
    assert iterator.pairs == [
        (0,),
        (1, 15),
        (2, 14),
        (3, 13),
        (4, 12),
        (5, 11),
        (6, 10),
        (7, 9),
        (8,),
    ]
