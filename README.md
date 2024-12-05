# ESP32 WROOM

```bash
python -m esptool \
    --chip esp32 \
    write_flash \
    0x1000 \
    ./firmware/ESP32_GENERIC-20241129-v1.24.1.bin
```

# ESP32 mini

```bash
python -m esptool \
    --chip esp32c3 \
    erase_flash

python -m esptool \
    --chip esp32c3 \
    write_flash \
    0x0 \
    ./firmware/ESP32_GENERIC_C3-20241129-v1.24.1.bin
```
