import asyncio

import bluetooth

from lib.context import on_board
from lib.pattern_index_manager import manage_index, write_index
from patterns_list import patterns
from screen.screen import screen, size
from vendor.aioble import aioble

_BLE_SERVICE_UUID = bluetooth.UUID("0823a10a-aebb-4f69-a511-dfa94c4141cd")
_BLE_LED_UUID = bluetooth.UUID("71321532-a5df-4af4-8ae1-e5e31ccfc7fd")

_ADV_INTERVAL_MS = 250_000

ble_service = aioble.Service(_BLE_SERVICE_UUID)
led_characteristic = aioble.Characteristic(
    ble_service, _BLE_LED_UUID, read=True, write=True, notify=True, capture=True
)
aioble.register_services(ble_service)


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
    for value in [0, 1]:
        on_board.value(value)
        await asyncio.sleep_ms(1000)


async def peripheral_task():
    """Await connection maybe."""
    while True:
        try:
            async with await aioble.advertise(
                _ADV_INTERVAL_MS,
                name="Goggles",
                services=[_BLE_SERVICE_UUID],
            ) as connection:
                print("Connection from", connection.device)
                await blink_onboard()
                await connection.disconnected()
        except asyncio.CancelledError:
            # Catch the CancelledError
            print("Peripheral task cancelled")
        except Exception as e:  # noqa: BLE001
            print("Error in peripheral_task:", e)
        finally:
            # Ensure the loop continues to the next iteration
            await asyncio.sleep_ms(100)


def _decode_data(data):
    try:
        if data is not None:
            # Decode the UTF-8 data
            return int.from_bytes(data, "big")
    except Exception as e:  # noqa: BLE001
        print("Error decoding temperature:", e)
        return None


async def wait_for_write():
    """Receive data."""
    while True:
        try:
            connection, data = await led_characteristic.written()
            print(data)
            print(type)
            data = _decode_data(data)
            print("Connection: ", connection)
            print("Data: ", data)

            write_index(data)

        except asyncio.CancelledError:
            # Catch the CancelledError
            print("Peripheral task cancelled")
        except Exception as e:  # noqa: BLE001
            print("Error in peripheral_task:", e)
        finally:
            # Ensure the loop continues to the next iteration
            await asyncio.sleep_ms(100)


async def main():
    """Run."""
    pattern = get_pattern()
    t1 = asyncio.create_task(pattern())
    t2 = asyncio.create_task(peripheral_task())
    t3 = asyncio.create_task(wait_for_write())
    await asyncio.gather(t1, t2, t3)


asyncio.run(main())
