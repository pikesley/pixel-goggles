def bytes_to_bits(byte_list):
    """Turn bytes into lists of bits."""
    return [[int(i) for i in list(f"{byte:#010b}"[2:])] for byte in byte_list]


def scale_bits(bits, scale):
    """Scale lists of bits."""
    scaled_bits = []
    for line in bits:
        scaled_bits.append([])
        for bit in line:
            for _ in range(scale):
                scaled_bits[-1].append(bit)

        for _ in range(scale - 1):
            scaled_bits.append(scaled_bits[-1])

    return scaled_bits


def colour_bits(bits, on_colour, off_colour):
    """Apply colours to bits."""
    if isinstance(on_colour, int):
        on_colour = (on_colour,)
    if isinstance(off_colour, int):
        off_colour = (off_colour,)

    coloured_bits = []
    for line in bits:
        coloured_bits.append([])
        for bit in line:
            if bit == 0:
                for element in off_colour:
                    coloured_bits[-1].append(element)
            if bit == 1:
                for element in on_colour:
                    coloured_bits[-1].append(element)

    return coloured_bits


def assemble_string(*characters):
    """Assemble characters into horizontal strings."""
    string = []
    for i in range(len(characters[0])):
        string.append([])
        for character in characters:
            string[-1] += character[i]

    return string
