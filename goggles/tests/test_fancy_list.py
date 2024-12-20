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

    assert list(rl) == ["b", "c"]

    rl.trim(end="back")
    assert list(rl) == ["b"]


def test_circularity():
    """Test it loops forever."""
    rl = FancyList(["a", "b", "c", "d"], circular=True)

    assert rl[2] == "c"
    assert rl[6] == "c"


def test_resetting():
    """Test it resets."""
    fl = FancyList(list("abcdefghijkl"))
    fl.rotate()
    fl.rotate()
    fl.rotate()

    assert list(fl) == (["d", "e", "f", "g", "h", "i", "j", "k", "l", "a", "b", "c"])

    fl.reset()
    assert list(fl) == (["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"])
