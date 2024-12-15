from lib.fancy_list import FancyList


def test_construction():
    """Test construction."""
    rl = FancyList(["a", "b", "c"])
    assert rl[0] == "a"
    assert rl.head == "a"


def test_rotation():
    """Test we can rotate."""
    rl = FancyList(["a", "b", "c"])
    rl.rotate()
    assert rl[0] == "b"

    rl.rotate(direction="r", steps=2)
    assert rl[0] == "c"


def test_trimming():
    """Test we can trim."""
    rl = FancyList(["a", "b", "c"])
    rl.trim()

    assert rl.items == ["b", "c"]

    rl.trim(end="back")
    assert rl.items == ["b"]
