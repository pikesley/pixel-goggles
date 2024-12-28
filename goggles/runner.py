import time

from lib.context import on_board
from lib.pattern_index_manager import manage_index
from patterns_list import patterns
from screen.lib.screen import screen


def run():
    """Do the work."""
    blink_onboard()
    index = manage_index(patterns)

    try:
        pattern = patterns[index]
    except IndexError:
        pattern = patterns[0]

    update_screen(pattern)
    pattern()


def blink_onboard(duration=100):
    """Blink the onboard LED."""
    for value in [0, 1]:
        on_board.value(value)
        time.sleep_ms(duration)


def update_screen(pattern):
    """Update the screen."""
    screen.write_text(
        pattern.__name__.replace("_", " "),
        x="centered",
        y="centered",
        colour=(255, 255, 255),
    )
