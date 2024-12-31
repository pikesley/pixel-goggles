import asyncio

from lib.bluetooth_controller import (
    await_connection,
    ble_service,
    wait_for_write,
)
from lib.pattern_index_manager import manage_index
from patterns_list import patterns
from vendor.aioble import aioble


def get_pattern():
    """Do the work."""
    index = manage_index(patterns)

    try:
        pattern = patterns[index]
    except IndexError:
        pattern = patterns[0]

    return pattern


def title_case(name):
    """Fix up name."""
    return " ".join([s[0].upper() + s[1:].lower() for s in name.split("_")])


async def main():
    """Run."""
    pattern = get_pattern()
    t1 = asyncio.create_task(pattern())
    t2 = asyncio.create_task(await_connection())
    t3 = asyncio.create_task(wait_for_write())
    await asyncio.gather(t1, t2, t3)


aioble.register_services(ble_service)
asyncio.run(main())
