state_file = "pattern-index"


def read_index():
    """Get the current index."""
    try:
        file = open(state_file)  # noqa: SIM115, PTH123
        index = int(file.read())
    except OSError:
        index = 0

    return index


def write_index(current_index, length):
    """Write the next index."""
    file = open(state_file, "w")  # noqa: SIM115, PTH123
    file.write(str((current_index + 1) % length))
    file.close()


def handle_index(patterns):
    """Handle the stateful indexing."""
    index = read_index()
    write_index(index, len(patterns))

    return index
