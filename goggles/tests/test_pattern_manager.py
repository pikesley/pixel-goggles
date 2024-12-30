from lib.pattern_manager import PatternManager


def foo():
    """Foo."""


def bar():
    """Bar."""


def baz():
    """Baz."""


patterns_list = [foo, bar, baz]


def test_names():
    """Test it gets a list of names."""
    pm = PatternManager(patterns_list)
    assert pm.names == ["foo", "bar", "baz"]


def test_index_lookup():
    """Test it finds indexes from names."""
    pm = PatternManager(patterns_list)
    assert pm.index_by_name("bar") == 1

    assert pm.index_by_name("nope") == 0
