import time

from lib.tilt_sensor import tilt_sensor

# I think the device might need calibrating
limits = {"x": {"anti-clockwise": -235, "clockwise": 270}}

# lookups =


def tilter():
    """Tilt."""
    while True:
        print(tilt_sensor.values)
        time.sleep_ms(100)
