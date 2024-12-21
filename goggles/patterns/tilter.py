from lib.tilt_sensor import tilt_sensor


def tilter():
    """Tilt."""
    while True:
        print(tilt_sensor.values)
