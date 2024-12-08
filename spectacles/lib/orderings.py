ring_size = 16
tops = {"right": 10, "left": 22}


def get_ordering(side, start, direction):  # noqa: ARG001
    """Calculate an ordering."""
    prime = tops[side]
    ordering = [prime]
    tail = list(range(prime - 1, -1, -1)) + list(range(ring_size - 1, prime, -1))

    if "anti" in direction:
        tail.reverse()

    return ordering + tail


# orderings = {
#     "left-hand": {
#         "clockwise": clockwise_left_hand,
#         "anticlockwise": list(reversed(clockwise_left_hand[1:]))
#         + [clockwise_left_hand[0]],
#     },
#     "right-hand": {
#         "clockwise": clockwise_right_hand,
#         "anticlockwise": list(reversed(clockwise_right_hand[1:]))
#         + [clockwise_right_hand[0]],
#     },
# }
