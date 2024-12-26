def bytes_to_bits(bytes):
    """Turn bytes into lists of bits."""
    return [list(f"{i:#010b}"[2:]) for i in bytes]


def scale_bits(bits, scale):
    """Scale lists of bits."""
    scaled_bits = []
    for line in bits:
        scaled_bits.append([])
        for bit in line:
            for i in range(scale):
                scaled_bits[-1].append(bit)

        for j in range(scale - 1):
            scaled_bits.append(scaled_bits[-1])

    return scaled_bits
