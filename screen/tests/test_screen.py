from unittest.mock import MagicMock, call

from lib.screen import ST7789v2


def test_initialisation():
    """Test screen initialises."""
    mocked_i2c = MagicMock()
    _ = ST7789v2(i2c=mocked_i2c)

    assert mocked_i2c.mock_calls == [
        call.writeto_mem(62, 34, bytearray(b"\xff")),
        call.writeto_mem(62, 32, bytearray(b"\x00")),
        call.writeto_mem(62, 54, bytearray(b"\x01")),
        call.writeto_mem(62, 105, bytearray(b"\x00\x00\xf0\x87\x00")),
    ]


def test_different_starting_background():
    """Test we can start with a different colour."""
    mocked_i2c = MagicMock()
    _ = ST7789v2(i2c=mocked_i2c, background_colour=(255, 0, 0))

    assert mocked_i2c.mock_calls[-1] == call.writeto_mem(
        62, 105, bytearray(b"\x00\x00\xf0\x87\xe0")
    )


def test_clearing_screen():
    """Test we can clear the screen."""
    mocked_i2c = MagicMock()
    st = ST7789v2(i2c=mocked_i2c, background_colour=(255, 0, 0))
    st.clear_screen()

    assert mocked_i2c.mock_calls[-1] == call.writeto_mem(
        62, 105, bytearray(b"\x00\x00\xf0\x87\xe0")
    )


def test_clearing_screen_with_a_different_colour():
    """Test we clear the screen wth a different colour."""
    mocked_i2c = MagicMock()
    st = ST7789v2(i2c=mocked_i2c, background_colour=(255, 0, 0))
    st.clear_screen()

    assert mocked_i2c.mock_calls[-1] == call.writeto_mem(
        62, 105, bytearray(b"\x00\x00\xf0\x87\xe0")
    )

    st.clear_screen((0, 255, 0))
    assert mocked_i2c.mock_calls[-1] == call.writeto_mem(
        62, 105, bytearray(b"\x00\x00\xf0\x87\x1c")
    )

    assert st.background_colour == (0, 255, 0)
