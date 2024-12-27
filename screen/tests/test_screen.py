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
