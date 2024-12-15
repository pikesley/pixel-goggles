import ntptime


def sync():
    """Sync the clock."""
    ntptime.settime()
