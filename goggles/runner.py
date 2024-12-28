import time

from lib.context import on_board
from lib.pattern_index_manager import manage_index
from patterns_list import patterns
from screen.screen import screen, size


def run():
    """Do the work."""
    blink_onboard()
    index = manage_index(patterns)

    try:
        pattern = patterns[index]
    except IndexError:
        pattern = patterns[0]

    update_screen(index)
    pattern()


def blink_onboard(duration=100):
    """Blink the onboard LED."""
    for value in [0, 1]:
        on_board.value(value)
        time.sleep_ms(duration)


def update_screen(index):
    """Update the screen."""
    now_pattern = patterns[index].__name__
    next_pattern = patterns[(index + 1) % len(patterns)].__name__

    screen.write_text(
        title_case(now_pattern)[:14],
        x="centered",
        y="centered",
        colour=(255, 0, 255),
        scale_factor=2,
    )

    screen.write_text(
        title_case(next_pattern),
        x="centered",
        y=size["y"] - 24,
        colour=(0, 0, 255),
        scale_factor=2,
    )


def title_case(name):
    """Fix up name."""
    return " ".join([s[0].upper() + s[1:].lower() for s in name.split("_")])
