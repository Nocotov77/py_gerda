from PIL import Image, ImageDraw


s = int(input())
new_image = Image.new("RGB", (20 * s, 20 * s), '#FFFFFF')
draw = ImageDraw.Draw(new_image)
col_l = '#000000'
siz = int(0.6 * s)
draw.arc((3 * s, 1 * s, 17 * s, 15 * s), 180, 0, fill=col_l, width=siz)
draw.arc(((3 * s, -3 * s), (17 * s, 19 * s)), 0, 180, fill=col_l, width=siz)

draw.chord((1 * s, 10 * s, 9 * s, 20 * s), 270, 270 + 90, fill=col_l, width=1)
draw.chord((5 * s, 5 * s, 13 * s, 15 * s), 90, 180, fill=col_l, width=1)
draw.ellipse(((6 * s, 11 * s), (7 * s, 12 * s)), fill='#FFFFFF', width=1)

draw.chord((11 * s, 10 * s, 19 * s, 20 * s), 180, 270, fill=col_l, width=1)
draw.chord((7 * s, 5 * s, 15 * s, 15 * s), 0, 90, fill=col_l, width=1)
draw.ellipse(((13 * s, 11 * s), (14 * s, 12 * s)), fill='#FFFFFF', width=1)

draw.chord((9 * s, 16 * s, 11 * s, 18 * s), 30, 120 + 30, fill=col_l, width=1)
draw.chord((9 * s, 17 * s, 11 * s, 19 * s), 210, 210 + 120, fill=col_l, width=1)

new_image.save('alien.png', "PNG")
