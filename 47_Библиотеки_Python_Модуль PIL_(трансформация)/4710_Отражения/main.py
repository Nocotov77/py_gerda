from PIL import Image


def reflect(image_name, kind=1):
    img = Image.open(image_name)

    if kind == 1:
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
    elif kind == 2:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif kind == 3:
        img = img.rotate(180)

    img.save("result.png")