ring_size = 16
tops = {"right": 10, "left": 22}


def get_prime(side, start):
    """Work out the prime position."""
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

    prime = (tops[side] + offsets[start]) % ring_size

    if side == "left":
        prime += ring_size

    return int(prime)


def get_ordering(side, start, direction):
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

    return ordering + tail
