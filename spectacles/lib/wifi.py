import secrets

import network


def connect():
    """Connect to wifi."""
    wlan = network.WLAN(network.WLAN.IF_STA)
    wlan.active(True)  # noqa: FBT003
    wlan.connect(secrets.SSID, secrets.KEY)
