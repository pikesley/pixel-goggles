from lib.rotatable_list import RotatableList


def test_construction():
    """Test construction."""
    rl = RotatableList(["a", "b", "c"])
    assert rl[0] == "a"
    assert rl.head == "a"


def test_rotation():
    """Test we can rotate."""
    rl = RotatableList(["a", "b", "c"])
    rl.rotate()
    assert rl[0] == "b"

    rl.rotate(direction="r", steps=2)
    assert rl[0] == "c"
