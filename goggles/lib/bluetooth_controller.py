import asyncio

import bluetooth
import machine
from vendor.aioble import aioble

from lib.context import bluetooth_uuids, on_board
from lib.pattern_index_manager import write_index
from patterns_list import pattern_by_name

_BLE_SERVICE_UUID = bluetooth.UUID(bluetooth_uuids["service"])
_BLE_PATTERN_UUID = bluetooth.UUID(bluetooth_uuids["pattern"])

_ADV_INTERVAL_MS = 25_000

ble_service = aioble.Service(_BLE_SERVICE_UUID)
pattern_write_characteristic = aioble.Characteristic(
    ble_service, _BLE_PATTERN_UUID, read=True, write=True, notify=True, capture=True
)


async def blink_onboard():
    """Blink the onboard LED."""
    for value in [0, 1]:
        on_board.value(value)
        await asyncio.sleep_ms(1000)


async def await_connection():
    """Await connection."""
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


async def wait_for_write():
    """Receive data."""
    while True:
        try:
            _, data = await pattern_write_characteristic.written()
            print(data)
            data = data.decode()
            print(data)

            write_index(pattern_by_name(data))
            machine.reset()

        except asyncio.CancelledError:
            # Catch the CancelledError
            print("Peripheral task cancelled")

        except Exception as e:  # noqa: BLE001
            print("Error in peripheral_task:", e)

        finally:
            # Ensure the loop continues to the next iteration
            await asyncio.sleep_ms(100)
