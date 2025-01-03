from helpers.fake_pixels import FakePixels

from lib.goggles import Goggles


def test_filling():
    """Test they fill good."""
    pixels = FakePixels(32)
    goggles = Goggles(pixels)

    goggles.fill((1, 0, 0))

    assert (
        pixels
        == [
            (1, 0, 0),
        ]
        * 32
    )

    colours = [(i * 10, 0, 0) for i in range(32)]
    goggles.fill(colours)

    assert pixels == [
        # left eye
        (140, 0, 0),
        (150, 0, 0),
        (0, 0, 0),
        (10, 0, 0),
        (20, 0, 0),
        (30, 0, 0),
        (40, 0, 0),
        (50, 0, 0),
        (60, 0, 0),
        (70, 0, 0),
        (80, 0, 0),
        (90, 0, 0),
        (100, 0, 0),
        (110, 0, 0),
        (120, 0, 0),
        (130, 0, 0),
        # right eye
        (180, 0, 0),
        (190, 0, 0),
        (200, 0, 0),
        (210, 0, 0),
        (220, 0, 0),
        (230, 0, 0),
        (240, 0, 0),
        (250, 0, 0),
        (260, 0, 0),
        (270, 0, 0),
        (280, 0, 0),
        (290, 0, 0),
        (300, 0, 0),
        (310, 0, 0),
        (160, 0, 0),
        (170, 0, 0),
    ]
