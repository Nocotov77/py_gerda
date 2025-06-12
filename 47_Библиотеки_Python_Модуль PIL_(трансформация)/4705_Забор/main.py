from PIL import Image, ImageDraw, ImageFont


def draw_on_image(image_path, output_path, color):
    img = Image.open(image_path)
    img = img.convert('RGB')
    draw = ImageDraw.Draw(img)

    x, y = img.size

    c = 0
    while c <= x:
        draw.rectangle((c, 480, c + 30, y), color)
        c += 50

    img.save(output_path)


col = input()
draw_on_image('flowers.png', 'fence.png', col)
