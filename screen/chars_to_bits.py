from pathlib import Path
import json

chars = json.loads(Path("conf", "font.json").read_text())

full_data = {}

for key, data in chars.items():
    full_data[key] = []
    bits = [list(f"{i:#010b}"[2:]) for i in chars["a"]]
    for line in bits:
        line = [[i] * 2 for i in line]
        line = sum(line, [])
        full_data[key].append(line)
        full_data[key].append(line)

Path("conf", "full-font.json").write_text(json.dumps(full_data))
