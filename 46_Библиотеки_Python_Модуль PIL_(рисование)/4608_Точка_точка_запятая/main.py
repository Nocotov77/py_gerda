from PIL import Image, ImageDraw


def human(bg_col, line_col, k, w):
    img = Image.new('RGB', (16 * k, 21 * k), bg_col)
    draw = ImageDraw.Draw(img)

    draw.line((8 * k, 5 * k, 8 * k, 11 * k), fill=line_col, width=w)
    draw.ellipse((8 * k - k / 5, 11 * k - k / 5, 8 * k + k / 5, 11 * k + k / 5), outline=line_col, width=w)
    draw.line((8 * k, 11 * k, 11 * k, 10 * k), fill=line_col, width=w)
    draw.ellipse((11 * k - k / 5, 10 * k - k / 5, 11 * k + k / 5, 10 * k + k / 5), outline=line_col, width=w)
    draw.line((11 * k, 10 * k, 13 * k, 15 * k), fill=line_col, width=w)
    draw.ellipse((13 * k - k / 5, 15 * k - k / 5, 13 * k + k / 5, 15 * k + k / 5), outline=line_col, width=w)
    draw.line((13 * k, 15 * k, 15 * k, 14 * k), fill=line_col, width=w)

    draw.line((7 * k, 6 * k, 9 * k, 6 * k), fill=line_col, width=w)
    draw.ellipse((9 * k - k / 5, 6 * k - k / 5, 9 * k + k / 5, 6 * k + k / 5), outline=line_col, width=w)
    draw.ellipse((7 * k - k / 5, 6 * k - k / 5, 7 * k + k / 5, 6 * k + k / 5), outline=line_col, width=w)
    draw.line((7 * k, 6 * k, 4 * k, 10 * k), fill=line_col, width=w)
    draw.ellipse((4 * k - k / 5, 10 * k - k / 5, 4 * k + k / 5, 10 * k + k / 5), outline=line_col, width=w)
    draw.line((4 * k, 10 * k, 6 * k, 13 * k), fill=line_col, width=w)

    draw.line((9 * k, 6 * k, 12 * k, 10 * k), fill=line_col, width=w)
    draw.ellipse((12 * k - k / 5, 10 * k - k / 5, 12 * k + k / 5, 10 * k + k / 5), outline=line_col, width=w)
    draw.line((12 * k, 10 * k, 15 * k, 7 * k), fill=line_col, width=w)

    draw.line((8 * k, 11 * k, 6 * k, 15 * k), fill=line_col, width=w)
    draw.ellipse((6 * k - k / 5, 15 * k - k / 5, 6 * k + k / 5, 15 * k + k / 5), outline=line_col, width=w)
    draw.line((6 * k, 15 * k, 5 * k, 20 * k), fill=line_col, width=w)
    draw.ellipse((5 * k - k / 5, 20 * k - k / 5, 5 * k + k / 5, 20 * k + k / 5), outline=line_col, width=w)
    draw.line((5 * k, 20 * k, 7 * k, 20 * k), fill=line_col, width=w)

    draw.ellipse((6 * k, k, 10 * k, 5 * k), outline=line_col, width=w)
    draw.ellipse((7 * k - k / 5, 3 * k - k / 5, 7 * k + k / 5, 3 * k + k / 5), fill=line_col, width=w)
    draw.ellipse((9 * k - k / 5, 3 * k - k / 5, 9 * k + k / 5, 3 * k + k / 5), fill=line_col, width=w)

    draw.arc((6 * k, k - k / 4, 10 * k, 4.5 * k), 45, 135, fill=line_col, width=w)

    img.save('human.png')
