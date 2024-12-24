def rle_compress(image):
    """
    Function to perform Run-Length Encoding (RLE) compression on a given image.

    Parameters:
    - image: str
        The path or filename of the BMP image file.

    Returns:
    - str:
        The compressed data in RLE format.

    Raises:
    - FileNotFoundError:
        If the specified image file is not found.
    """

    try:
        # Open the image file in binary mode
        with open(image, "rb") as file:
            # Read the image data
            data = file.read()

        # Perform RLE compression on the image data
        compressed_data = ""
        count = 1
        for i in range(1, len(data)):
            if data[i] == data[i - 1]:
                count += 1
            else:
                compressed_data += str(count) + data[i - 1].to_bytes(1, "big").decode(
                    "latin-1"
                )
                count = 1

        # Add the last run of data to the compressed data
        compressed_data += str(count) + data[-1].to_bytes(1, "big").decode("latin-1")

        return compressed_data

    except FileNotFoundError:
        raise FileNotFoundError("Image file not found.")


# Example usage:
image_file = "random.bmp"
compressed_data = rle_compress(image_file)
print("Compressed data:", compressed_data)
