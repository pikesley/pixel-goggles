import asyncio

from vendor.aioble import aioble

from lib.bluetooth_controller import await_connection, ble_service, wait_for_write
from lib.pattern_index_manager import manage_index
from patterns_list import patterns


def get_pattern():
    """Select a pattern."""
    index = manage_index(patterns)

    try:
        pattern = patterns[index]
    except IndexError:
        pattern = patterns[0]

    return pattern


async def main():
    """Run."""
    pattern = get_pattern()
    t1 = asyncio.create_task(pattern())
    t2 = asyncio.create_task(await_connection())
    t3 = asyncio.create_task(wait_for_write())
    await asyncio.gather(t1, t2, t3)


aioble.register_services(ble_service)
asyncio.run(main())
