from PIL import Image, ImageDraw


def stripes(n, size, direction="v"):
    white = (255, 255, 255)
    black = (0, 0, 0)
    im = Image.new("RGB", size, white)
    draw = ImageDraw.Draw(im)

    if direction == "v":
        h = size[0] // n
        x = 0
        y = 0
        x1 = h
        y1 = size[1]
        for _ in range(n):
            draw.rectangle((x, y, x1, y1), fill=black, width=h)
            x = x + h
            x1 = x1 + h
            draw.rectangle((x, y, x1, y1), fill=white, width=h)
            x = x + h
            x1 = x1 + h

    else:
        h = size[1] // n
        x = 0
        y = 0
        x1 = size[0]
        y1 = h

        for _ in range(n):
            draw.rectangle((x, y, x1, y1), fill=black, width=h)
            y = y + h
            y1 = y1 + h
            draw.rectangle((x, y, x1, y1), fill=white, width=h)
            y = y + h
            y1 = y1 + h

    im.save("zebra.png")