from PIL import Image


def snow_forest(position, snow_alpha):
    forest = Image.open("forest.png").convert("RGB")
    snow = Image.open("snow.png").convert("RGBA")
    snow = snow.resize((100, 100), Image.LANCZOS)

    forest_crop = forest.crop((position[0], position[1], position[0] + 100, position[1] + 100))

    blended = Image.new("RGBA", (100, 100))
    for x in range(100):
        for y in range(100):
            r1, g1, b1, a1 = snow.getpixel((x, y))
            r2, g2, b2 = forest_crop.getpixel((x, y))
            r = int(r1 * snow_alpha / 100 + r2 * (1 - snow_alpha / 100))
            g = int(g1 * snow_alpha / 100 + g2 * (1 - snow_alpha / 100))
            b = int(b1 * snow_alpha / 100 + b2 * (1 - snow_alpha / 100))
            blended.putpixel((x, y), (r, g, b, a1))

    forest.paste(blended, position, blended)
    forest.save("output.png")