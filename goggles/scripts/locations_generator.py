import json
from math import atan2, cos, degrees, radians, sin
from pathlib import Path

nose_band = 3
diameter = 4.5

mappings = {
    "left": {
        "point": "w",
        "direction": "clockwise",
        "points": [
            "e",
            "ene",
            "ne",
            "nne",
            "n",
            "nnw",
            "nw",
            "wnw",
            "w",
            "wsw",
            "sw",
            "ssw",
            "s",
            "sse",
            "se",
            "ese",
        ],
    },
    "right": {
        "point": "e",
        "direction": "anticlockwise",
        "points": [
            "w",
            "wnw",
            "nw",
            "nnw",
            "n",
            "nne",
            "ne",
            "ene",
            "e",
            "ese",
            "se",
            "sse",
            "s",
            "ssw",
            "sw",
            "wsw",
        ],
    },
}

points = [
    "e",
    "ene",
    "ne",
    "nne",
    "n",
    "nnw",
    "nw",
    "wnw",
    "w",
    "wsw",
    "sw",
    "ssw",
    "s",
    "sse",
    "se",
    "ese",
]


unit_circle = {}

increment = 360 / 16
for index, point in enumerate(points):
    x = cos(radians(index * increment))
    y = sin(radians(index * increment))

    unit_circle[point] = {"x": x, "y": y}


offset = (nose_band / 2) + (diameter / 2)

offsets = {"left": 0 - offset, "right": offset}

results = {"left": {}, "right": {}}

max_x = 0
max_y = 0

for side, offset in offsets.items():
    for point, coords in unit_circle.items():
        scaled_y = coords["y"] * 2.25
        scaled_x = (coords["x"] * 2.25) + offset

        max_x = max(scaled_x, max_x)

        max_y = max(scaled_y, max_y)

        results[side][point] = {
            "x": round(scaled_x, 8),
            "y": round(scaled_y, 8),
        }
        angle = degrees(atan2(scaled_y, scaled_x)) % 360

        results[side][point]["angle"] = round(angle, 8)

final_locations = []

for side in ["left", "right"]:
    mapping = json.loads(
        Path(
            "conf",
            "renders",
            "eyes",
            side,
            mappings[side]["point"],
            f'{mappings[side]["direction"]}.json',
        ).read_text(encoding="utf-8")
    )

    for index, point in enumerate(mappings[side]["points"]):
        data = {
            "index": mapping[index],
            "side": side,
            "point": point,
        }
        data.update(results[side][point])

        final_locations.append(data)

final_locations.sort(key=lambda x: x["index"])

normalised_locations = []
for item in final_locations:
    item["x"] = round(item["x"] / max_x, 8)
    item["y"] = round(item["y"] / max_y, 8)

    normalised_locations.append(item)

Path("conf", "locations.json").write_text(
    json.dumps(normalised_locations, indent=2), encoding="utf-8"
)


outpath = Path("conf", "locations")
outpath.mkdir(parents=True, exist_ok=True)

for key in normalised_locations[0]:
    if key != "index":
        Path(outpath, f"{key}s.json").write_text(
            json.dumps([i[key] for i in normalised_locations], indent=2),
            encoding="utf-8",
        )

# reference_angles = {
#     "right": {
#         "w": 0.0,
#         "wnw": 27.25,
#         "nw": 36.38,
#         "nnw": 35.73,
#         "n": 30.96,
#         "nne": 24.26,
#         "ne": 16.59,
#         "ene": 8.40,
#         "e": 0.0,
#         "ese": 351.6,
#         "se": 343.41,
#         "sse": 335.73,
#         "s": 329.04,
#         "ssw": 324.26,
#         "sw": 323.61,
#         "wsw": 332.74,
#     },
#     "left": {
#         "e": 180.0,
#         "ene": 152.74,
#         "ne": 143.61,
#         "nne": 144.26,
#         "n": 149.03,
#         "nnw": 155.73,
#         "nw": 163.41,
#         "wnw": 171.59,
#         "w": 180.0,
#         "wsw": 188.40,
#         "sw": 196.59,
#         "ssw": 204.26,
#         "s": 210.96,
#         "sse": 215.74,
#         "se": 216.38,
#         "ese": 207.26,
#     },
# }

# for side in ["right", "left"]:
#     for point in ["n", "ne", "e", "se", "s", "sw", "w", "nw"]:
#         text = f"{side}::{point}"
#         result = results[side][point]["angle"]
#         reference = reference_angles[side][point]
#         print(f"{text} {result} :: {reference}")
