from PIL import Image, ImageDraw

n = int(input())
сolor_left = input()
color_right = input()
width, height = 400, (200 + n * 250 + ((n - 1) * 130))
im = Image.new('RGB', (width, height), '#777777')
draw = ImageDraw.Draw(im)
x1, y1, x2, y2 = 100, 100, 300, 300
step = 0
for i in range((n + n - 1)):
    if i > 0:
        step += 190

    if i % 2 == 0:
        draw.arc([70, 100 + step, 330, 350 + step], start=90, end=270, fill=сolor_left, width=60)
    else:
        draw.arc([70, 100 + step, 330, 350 + step], start=-90, end=90, fill=color_right, width=60)

output_filename = "colored_snake.png"
im.save(output_filename)