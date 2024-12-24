r = [255, 0, 0]
g = [0, 255, 0]
b = [0, 0, 255]
w = [255, 255, 255]

pixels = [
    [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],
    [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],
    [g, g, w, w, w, w, w, w, w, w, w, w, w, w, g, g],
    [g, g, w, w, w, w, w, w, w, w, w, w, w, w, g, g],
    [g, g, w, w, w, w, w, w, w, w, w, w, w, w, g, g],
    [g, g, w, w, w, w, w, w, w, w, w, w, w, w, g, g],
    [g, g, w, w, w, w, w, w, w, w, w, w, w, w, g, g],
    [g, g, w, w, w, w, w, w, w, w, w, w, w, w, g, g],
    [g, g, w, w, w, w, w, w, w, w, w, w, w, w, g, g],
    [g, g, w, w, w, w, w, w, w, w, w, w, w, w, g, g],
    [g, g, w, w, w, w, w, w, w, w, w, w, w, w, g, g],
    [g, g, w, w, w, w, w, w, w, w, w, w, w, w, g, g],
    [g, g, w, w, w, w, w, w, w, w, w, w, w, w, g, g],
    [g, g, w, w, w, w, w, w, w, w, w, w, w, w, g, g],
    [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],
    [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],
]

image = sum(sum(pixels, []), [])
