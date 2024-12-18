import time

from lib.colour_tools import scale_colour, time_based_rgb
from lib.context import eyes, pixels
from lib.tools import inverse_square_tail


def pulse():
    """Pulse."""
    pulse_length = 100
    sleep_time = 5
    tail_coefficient = 0.07

    data = {
        "left": {
            "values": inverse_square_tail(pulse_length, coefficient=tail_coefficient),
            "colour-key": "bytes",
        },
        "right": {
            "values": inverse_square_tail(pulse_length, coefficient=tail_coefficient),
            "colour-key": "inverse",
        },
    }

    data["right"]["values"].rotate(
        steps=int(len(data["right"]["values"]) / 4), direction="r"
    )

    while True:
        colour = time_based_rgb(1.2)

        for i in range(len(data["left"]["values"])):
            for side in ["left", "right"]:
                eyes[side].fill(
                    scale_colour(
                        colour[data[side]["colour-key"]], data[side]["values"][i]
                    )
                )

            pixels.write()
            time.sleep_ms(sleep_time)
