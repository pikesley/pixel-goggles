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
    big_scale = 2
    small_scale = 1

    big_colour = (255, 0, 255)
    small_colour = (0, 0, 255)

    y_offset=48

    now_pattern = patterns[index].__name__
    next_pattern = patterns[(index + 1) % len(patterns)].__name__

    if "_" in now_pattern:
        now_pattern = now_pattern.split("_")
        y_offset = y_offset - (big_scale * 4)
    else:
        now_pattern = [now_pattern]

    try:
        for i, line in enumerate(now_pattern):
            print(line)
            y_val = y_offset + (i * 8 * big_scale)
            screen.write_text(
                title_case(line),
                x="centered",
                y=y_val,
                colour=big_colour,
                scale_factor=big_scale,
            )

        screen.write_text(
            title_case(next_pattern),
            x="centered",
            y=size["y"] - 32,
            colour=small_colour,
            scale_factor=small_scale,
        )
    except MemoryError:
        pass


def title_case(name):
    """Fix up name."""
    return " ".join([s[0].upper() + s[1:].lower() for s in name.split("_")])
