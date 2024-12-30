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


def write_next_index(current_index, length):
    """Write the next index."""
    write_index((current_index + 1) % length)


def manage_index(patterns):
    """Handle the stateful indexing."""
    index = read_index()
    write_next_index(index, len(patterns))

    return index


def write_index(index):
    """Write an arbitrary index."""
    state = {"pattern-index": index}
    file = open(state_file, "w")  # noqa: SIM115, PTH123
    file.write(json.dumps(state))
    file.close()
