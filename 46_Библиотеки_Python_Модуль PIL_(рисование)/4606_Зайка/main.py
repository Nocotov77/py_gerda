from PIL import Image, ImageDraw

s = int(input())

width, height = 37 * s, 27 * s
im = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(im)
yellow = (255, 242, 204)
purple = (254, 214, 244)
draw.ellipse([8 * s, 12 * s, 26 * s, 26 * s], fill=yellow, outline='black', width=2)
draw.ellipse([22 * s, 13 * s, 36 * s, 17 * s], fill=yellow, outline='black', width=2)
draw.ellipse([23 * s, 14 * s, 32 * s, 16 * s], fill=purple, outline='black', width=2)
draw.ellipse([10 * s, 1 * s, 14 * s, 15 * s], fill=yellow, outline='black', width=2)
draw.ellipse([11 * s, 5 * s, 13 * s, 14 * s], fill=purple, outline='black', width=2)
draw.ellipse([16 * s, 19 * s, 18 * s, 20 * s], fill=(192, 0, 0), outline='black', width=2)
draw.ellipse([14 * s, 17 * s, 15 * s, 18 * s], fill='black', outline='black', width=2)
draw.ellipse([19 * s, 17 * s, 20 * s, 18 * s], fill='black', outline='black', width=2)
draw.line([(10 * s, 19 * s), (15 * s, 20 * s)], fill='black', width=2)
draw.line([(11 * s, 22 * s), (15 * s, 21 * s)], fill='black', width=2)
draw.line([(19 * s, 21 * s), (23 * s, 22 * s)], fill='black', width=2)
draw.line([(19 * s, 20 * s), (24 * s, 19 * s)], fill='black', width=2)
draw.rectangle([(16 * s + (s / 2), 21 * s), (17 * s + (s / 2), 22 * s)], fill='white', outline='black', width=2)
draw.line([(17 * s, 20 * s), (17 * s, 22 * s)], fill='black', width=2)
output_filename = "cute_bunny.png"
im.save(output_filename)