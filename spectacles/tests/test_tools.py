from lib.tools import index_pairs


def test_index_pairs():
    """Test index_pairs."""
    assert index_pairs(12, 0) == [
        (0, 11),
        (1, 10),
        (2, 9),
        (3, 8),
        (4, 7),
        (5, 6),
    ]

    assert index_pairs(12, 4) == [
        (4, 3),
        (5, 2),
        (6, 1),
        (7, 0),
        (8, 11),
        (9, 10),
    ]
