from PIL import Image, ImageDraw

s = int(input())

width = 24 * s
height = 40 * s

im = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(im)

green = '#00b050'
brown = '#7f6000'

center_x = width // 2

top_height = 8 * s + 3 * s
vertices_top = [
    (center_x, 3 * s),
    (center_x - 6 * s, top_height),
    (center_x + 6 * s, top_height)
]
draw.polygon(vertices_top, fill=green)

medium_height = 12 * s + 8 * s
vertices_top = [
    (center_x, 8 * s),
    (center_x - 8 * s, medium_height),
    (center_x + 8 * s, medium_height)
]
draw.polygon(vertices_top, fill=green)

bottom_height = 16 * s + 16 * s
vertices_bottom = [
    (center_x, 16 * s),
    (center_x - 10 * s, bottom_height),
    (center_x + 10 * s, bottom_height)
]
draw.polygon(vertices_bottom, fill=green)

trunk_height = 4 * s
trunk_width = 3 * s
trunk_y = bottom_height
draw.rectangle(
    (center_x - trunk_width // 2, trunk_y, center_x + trunk_width // 2, trunk_y + trunk_height),
    fill=brown
)

im.save('fir_tree.png')