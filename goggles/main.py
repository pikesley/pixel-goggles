import asyncio
from random import randint

from lib.context import on_board
from lib.pattern_index_manager import manage_index
from patterns_list import patterns
from screen.screen import screen, size


def get_pattern():
    """Do the work."""
    index = manage_index(patterns)

    try:
        pattern = patterns[index]
    except IndexError:
        pattern = patterns[0]

    update_screen(index)
    return pattern


def update_screen(index):
    """Update the screen."""
    big_scale = 2
    small_scale = 1

    big_colour = (255, 0, 255)
    small_colour = (0, 0, 255)

    y_offset = 48

    now_pattern = patterns[index].__name__
    next_pattern = patterns[(index + 1) % len(patterns)].__name__

    if "_" in now_pattern:
        now_pattern = now_pattern.split("_")
        y_offset = y_offset - (big_scale * 4)
    else:
        now_pattern = [now_pattern]

    try:
        for i, line in enumerate(now_pattern):
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


async def blink_onboard():
    """Blink the onboard LED."""
    # placeholder for bluetooth later
    while True:
        for value in [0, 1]:
            on_board.value(value)
            await asyncio.sleep_ms(randint(0, 1000))  # noqa: S311


async def main():
    """Run."""
    pattern = get_pattern()
    t1 = asyncio.create_task(pattern())
    t2 = asyncio.create_task(blink_onboard())
    await asyncio.gather(t1, t2)


asyncio.run(main())
