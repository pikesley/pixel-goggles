import json

state_file = "state.json"


def read_index():
    """Get the current index."""
    try:
        file = open(state_file)  # noqa: SIM115, PTH123
        data = json.loads(file.read())
        index = data["pattern-index"]
    except OSError:
        index = 0

    return index


def write_index(current_index, length):
    """Write the next index."""
    state = {"pattern-index": (current_index + 1) % length}
    file = open(state_file, "w")  # noqa: SIM115, PTH123
    file.write(json.dumps(state))
    # file.write(str((current_index + 1) % length))
    file.close()


def manage_index(patterns):
    """Handle the stateful indexing."""
    index = read_index()
    write_index(index, len(patterns))

    return index
