from random import randint

ring_size = 16
tops = {"right": 10, "left": 22}


offsets = {
    "n": 0,
    "nnw": 1,
    "nw": 2,
    "wnw": 3,
    "w": 4,
    "wsw": 5,
    "sw": 6,
    "ssw": 7,
    "s": 8,
    "sse": 9,
    "se": 10,
    "ese": 11,
    "e": 12,
    "ene": 13,
    "ne": 14,
    "nne": 15,
}

# FancyList?
compass_points = list(offsets.keys())


def random_origin():
    """Get a random compass point."""
    return compass_points[randint(0, len(compass_points) - 1)]  # noqa: S311


def random_rotation():
    """Get a random rotation direction."""
    rotation = "clockwise"
    if randint(0, 1) == 0:  # noqa: S311
        rotation = f"anti{rotation}"

    return rotation


def get_prime(side, start):
    """Work out the prime position."""
    prime = (tops[side] + offsets[start]) % ring_size

    if side == "left":
        prime += ring_size

    return int(prime)


def get_ordering(side, start, direction="clockwise", overlap=False):  # noqa: FBT002
    """Calculate an ordering."""
    offset = 0
    if side == "left":
        offset = ring_size

    prime = get_prime(side, start)
    ordering = [prime]
    tail = list(range(prime - 1, -1 + offset, -1)) + list(
        range(ring_size - 1 + offset, prime, -1)
    )

    if "anti" in direction:
        tail.reverse()

    result = ordering + tail

    if overlap:
        result += [result[0]]

    return result


def get_pairs(side, start):
    """Get pairs across the ring."""
    ordering = get_ordering(side, start)
    chunk_size = int((ring_size / 2) - 1)
    first_chunk = ordering[1 : chunk_size + 1]
    second_chunk = list(reversed(ordering[chunk_size + 2 :]))

    pairs = [(ordering[0],)]

    for i in range(chunk_size):
        pairs.append((first_chunk[i], second_chunk[i]))  # noqa: PERF401

    pairs.append((ordering[chunk_size + 1],))

    return pairs
