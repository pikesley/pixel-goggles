import asyncio

import bluetooth
import machine

from lib.context import on_board
from lib.pattern_index_manager import write_index
from lib.pattern_manager import PatternManager
from vendor.aioble import aioble

_BLE_SERVICE_UUID = bluetooth.UUID("0823a10a-aebb-4f69-a511-dfa94c4141cd")
_BLE_LED_UUID = bluetooth.UUID("71321532-a5df-4af4-8ae1-e5e31ccfc7fd")

_ADV_INTERVAL_MS = 250_000
ble_service = aioble.Service(_BLE_SERVICE_UUID)
led_characteristic = aioble.Characteristic(
    ble_service, _BLE_LED_UUID, read=True, write=True, notify=True, capture=True
)


pattern_manager = PatternManager()


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
            _, data = await led_characteristic.written()
            data = data.decode()

            write_index(pattern_manager.index_by_name(data))
            machine.reset()

        except asyncio.CancelledError:
            # Catch the CancelledError
            print("Peripheral task cancelled")

        except Exception as e:  # noqa: BLE001
            print("Error in peripheral_task:", e)

        finally:
            # Ensure the loop continues to the next iteration
            await asyncio.sleep_ms(100)
