from lib.colour_tools import get_sector, get_segments, rgb_from_degrees, rgb_from_hue


def test_get_sector():
    """Test we can get the sector."""
    assert get_sector(0) == 0
    assert get_sector(60) == 1
    assert get_sector(150) == 2  # noqa: PLR2004


def test_rgb_from_hue():
    """Test we can rgb from hue."""
    expectations = (
        (0, (255, 0, 0)),
        (1 / 3, (0, 255, 0)),
        (1 / 2, (0, 255, 255)),
        (2 / 3, (0, 0, 255)),
    )

    for expectation in expectations:
        assert rgb_from_hue(expectation[0], brightness=1.0)["bytes"] == expectation[1]


def test_get_segments():
    """Test we get the segments."""
    assert get_segments() == [
        {"offset": 0, "red": 1, "blue": 0},
        {"offset": 60, "blue": 0, "green": 1},
        {"offset": 120, "red": 0, "green": 1},
        {"offset": 180, "red": 0, "blue": 1},
        {"offset": 240, "blue": 1, "green": 0},
        {"offset": 300, "red": 1, "green": 0},
    ]


def test_rgb_from_degrees():
    """Test we get the RGBs."""
    assert rgb_from_degrees(0, brightness=1.0) == {
        "bytes": (255, 0, 0),
        "inverse": (0, 255, 255),
    }

    assert rgb_from_degrees(0, brightness=0.5) == {
        "bytes": (127, 0, 0),
        "inverse": (0, 127, 127),
    }
