clockwise_right_hand = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 15, 14, 13, 12, 11]
clockwise_left_hand = [22, 21, 20, 19, 18, 17, 16, 31, 30, 29, 28, 27, 26, 25, 24, 23]

orderings = {
    "left-hand": {
        "clockwise": clockwise_left_hand,
        "anticlockwise": list(reversed(clockwise_left_hand[1:]))  # noqa: RUF005
        + [clockwise_left_hand[0]],
    },
    "right-hand": {
        "clockwise": clockwise_right_hand,
        "anticlockwise": list(reversed(clockwise_right_hand[1:]))  # noqa: RUF005
        + [clockwise_right_hand[0]],
    },
}
