import json
from pathlib import Path

from lib.context import bluetooth_uuids
from patterns_list import patterns

data = {
    "uuids": bluetooth_uuids,
    "patterns": [p.__name__ for p in patterns],
}

Path("/opt/esp32/controller/html/data.json").write_text(
    json.dumps(data, indent=2, sort_keys=True), encoding="utf-8"
)
