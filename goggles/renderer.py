import json
from pathlib import Path

from lib.fancy_list import FancyList

ring_size = 16
compass_points = [
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
    "e",
    "ene",
    "ne",
    "nne",
]

tops = {"left": 2, "right": 30}


def make_left_anticlockwise():
    """Make left anticlockwise."""
    path_elements = []
    data = {}

    for index, point in enumerate(compass_points):
        path_elements.append(point)
        genesis = FancyList(list(range(len(compass_points))))
        genesis.rotate(steps=index + tops["left"], direction="l")

        data["/".join(path_elements)] = genesis

        path_elements.pop()

    genesis.rotate(direction="l")

    return data


def make_right_anticlockwise():
    """Make right anticlockwise."""
    lefts = make_left_anticlockwise()
    data = {}

    for key, values in lefts.items():
        ordering = FancyList(values.items)
        # `tops["right"] - tops["left"]` has magic-number energy
        # but I think
        # * the `left` orderings are all offset by `tops["left"]` so we take that off
        # * and then the right eye starts at `tops["left"]` so we add that on
        # but we also add the `ring_size` for the offset
        ordering.items = [
            ((x + (tops["right"] - tops["left"])) % ring_size) + ring_size
            for x in ordering.items
        ]
        data[key] = ordering

    return data


def make_clockwise(antis):
    """Make clockwise."""
    data = {}

    for key, values in antis.items():
        ordering = FancyList(values.items)
        ordering.reverse()
        ordering.rotate(direction="r")
        data[key] = ordering

    return data


def make_left_clockwise():
    """Make left clockwise."""
    return make_clockwise(make_left_anticlockwise())


def make_right_clockwise():
    """Make right clockwise."""
    return make_clockwise(make_right_anticlockwise())


def make_pairs(singles):
    """Make some pairs."""
    data = {}
    chunk_size = int((ring_size / 2) - 1)

    for key, values in singles.items():
        ordering = FancyList(values.items)

        first_chunk = ordering[1 : chunk_size + 1]
        second_chunk = list(reversed(ordering[chunk_size + 2 :]))

        pairs = [(ordering[0],)]
        for i in range(chunk_size):
            pairs.append(tuple(sorted((first_chunk[i], second_chunk[i]))))  # noqa: PERF401

        pairs.append((ordering[chunk_size + 1],))

        data[key] = FancyList(pairs)

    return data


def make_left_pairs():
    """Make left pairs."""
    return make_pairs(make_left_anticlockwise())


def make_right_pairs():
    """Make right pairs."""
    return make_pairs(make_right_anticlockwise())


def render():
    """Render."""
    data = {
        "left": {
            "clockwise": make_left_clockwise(),
            "anticlockwise": make_left_anticlockwise(),
            "pairs": make_left_pairs(),
        },
        "right": {
            "clockwise": make_right_clockwise(),
            "anticlockwise": make_right_anticlockwise(),
            "pairs": make_right_pairs(),
        },
    }

    path_elements = ["renders", "eyes"]

    for eye in data:
        path_elements.append(eye)

        for point in compass_points:
            path_elements.append(point)

            Path(*path_elements).mkdir(exist_ok=True, parents=True)

            for rotation in ["clockwise", "anticlockwise"]:
                path_elements.append(f"{rotation}.json")

                outpath = Path(*path_elements)
                print(str(outpath))
                outpath.write_text(
                    json.dumps(data[eye][rotation][point].items), encoding="utf-8"
                )

                path_elements.pop()

                path_elements.append("pairs.json")
                outpath = Path(*path_elements)

                print(str(outpath))
                outpath.write_text(
                    json.dumps(data[eye]["pairs"][point].items), encoding="utf-8"
                )

                path_elements.pop()

            path_elements.pop()

        path_elements.pop()


if __name__ == "__main__":
    render()
