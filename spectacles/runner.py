from lib.index_management import handle_index
from patterns.patterns import patterns


def run():
    """Do the work."""
    index = handle_index(patterns)

    try:
        pattern = patterns[index]
    except IndexError:
        pattern = patterns[0]

    pattern()
