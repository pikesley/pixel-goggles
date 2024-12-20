# import time

# from lib.colour_tools import just_an_rgb
# from lib.context import goggles, pixels, ring_size
# from lib.tools import inverse_square_tail, pendulum_timings

# offset = 2
# timing_scale = 7000

# tail_length = 8
# tail_off_factor = 2

# # left = get_ordering("left", "n", "clockwise", overlap=True)[offset:-offset]
# # right = get_ordering("right", "n", "clockwise", overlap=True)[offset:-offset]
# timings = pendulum_timings()

# tail = inverse_square_tail(tail_length)


# def pendulum():
#     """Spin the wheel."""
#     while True:
#         roll()
#         roll(direction="anti-clockwise")


# def roll(direction="clockwise"):
#     """Roll around."""
#     ranges = [range(offset, ring_size), range(ring_size - (1 + offset), 0, -1)]

#     for r in ranges:
#         for i in r:
#             colour = just_an_rgb()
#             goggles.off()
#             goggles.left[0] = (255, 255, 255)

#             goggles.left[i] = colour
#             goggles.right[i] = colour
#             pixels.write()

#             print(i, timings[i])

#             interval = int(timings[i] * timing_scale)
#             time.sleep_ms(interval)

#     # full_range = range(len(left))
#     # if "anti" in direction:
#     #     full_range = range(len(left) - 1, -1, -1)

#     # tail_count = 0

#     # for i in full_range:
#     #     off(pixels)

#     #     if tail_count < tail_length:
#     #         tail_count += 1

#     #     # paint_tail(i, tail_count, direction)

#     #     interval = int(timings[i] * timing_scale)
#     #     time.sleep_ms(interval)

#     # erase_tail(direction=direction)


# # def paint_tail(index, count, direction):
# #     """Paint the tail."""
# #     colour = just_an_rgb()

# #     for t in range(count):
# #         tail_index = index - t
# #         if "anti" in direction:
# #             tail_index = index + t

# #         for eye in [left, right]:
# #             pixels[eye[tail_index]] = scale_colour(colour, tail[t])

# #     pixels.write()


# # def erase_tail(direction):
# #     """Clean up the tail."""
# #     tail_count = tail_length
# #     while tail_count > 1:
# #         for eye in [left, right]:
# #             victim_index = eye[0 - (tail_count)]
# #             if "anti" in direction:
# #                 victim_index = eye[tail_count - 1]

# #             pixels[victim_index] = (0, 0, 0)

# #         pixels.write()
# #         tail_count -= 1
# #         time.sleep_ms(int(timing_scale / tail_off_factor))


# # def get_ordering(side, start, direction="clockwise", overlap=False):
# #     """Calculate an ordering."""
# #     offset = 0
# #     if side == "right":
# #         offset = ring_size

# #     prime = get_prime(side, start)
# #     ordering = [prime]
# #     tail = list(range(prime - 1, -1 + offset, -1)) + list(
# #         range(ring_size - 1 + offset, prime, -1)
# #     )

# #     if "anti" in direction:
# #         tail.reverse()

# #     result = ordering + tail

# #     if overlap:
# #         result += [result[0]]

# #     return result
