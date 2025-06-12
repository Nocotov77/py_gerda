
from PIL import Image


def color_gradient(output_file, crop_box, kind="linear", color="r"):
    gradient = Image.linear_gradient("L") if kind == "linear" else Image.radial_gradient("L")
    gradient = gradient.resize((256, 256), Image.LANCZOS)

    color_map = {"r": (255, 0, 0), "g": (0, 255, 0), "b": (0, 0, 255)}
    if color not in color_map:
        color = "r"

    r, g, b = color_map[color]
    colored_gradient = Image.new("RGB", (256, 256))
    for x in range(256):
        for y in range(256):
            intensity = gradient.getpixel((x, y))
            colored_gradient.putpixel((x, y), (r * intensity // 255, g * intensity // 255, b * intensity // 255))

    cropped = colored_gradient.crop(crop_box)
    cropped.save(output_file)