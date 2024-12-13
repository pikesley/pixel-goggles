import time

from lib.context import on_board
from lib.pattern_index_manager import manage_index
from patterns_list import patterns


def run():
    """Do the work."""
    blink_onboard()
    index = manage_index(patterns)

    try:
        pattern = patterns[index]
    except IndexError:
        pattern = patterns[0]

    pattern()


def blink_onboard(duration=100):
    """Blink the onboard LED."""
    for value in [0, 1]:
        on_board.value(value)
        time.sleep_ms(duration)
