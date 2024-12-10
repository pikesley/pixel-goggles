from lib.colour_tools import just_an_rgb


def rotate_list(start_list, direction="l", steps=1):
    """Rotate a list, a la `deque`."""
    if direction == "l":
        for _ in range(steps):
            start_list = start_list[1:] + [start_list[0]]
        return start_list

    for _ in range(steps):
        start_list = [start_list[-1]] + start_list[:-1]
    return start_list


def colour_pair(pixels, pair, colour=None):
    """Apply colour to some indeces."""
    if not colour:
        colour = just_an_rgb()

    for index in pair:
        pixels[index] = colour


def inverse_square_tail(length, coefficient=1, backwards=False):  # noqa: FBT002
    """Inverse-square tail-off values."""
    values = [1 / (2 ** (t * coefficient)) for t in range(length)]
    if backwards:
        values.reverse()

    return values
