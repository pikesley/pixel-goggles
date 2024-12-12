from lib.pattern_index_manager import manage_index
from patterns_list import patterns


def run():
    """Do the work."""
    index = manage_index(patterns)

    try:
        pattern = patterns[index]
    except IndexError:
        pattern = patterns[0]

    pattern()
