from PIL import Image


def less_variety(old_name, last_name):
    im = Image.open(old_name)
    x, y = im.size
    pix = im.load()
    count = set()
    for i in range(x):
        for j in range(y):
            r, g, b = pix[i, j]

            count.add((r, g, b))
    count = len(count)

    while count > 256:
        count //= 2

    im2 = im.resize((x // 2, y // 2)).quantize(count)

    im2.save(last_name)


less_variety("castle.png", "out.png")