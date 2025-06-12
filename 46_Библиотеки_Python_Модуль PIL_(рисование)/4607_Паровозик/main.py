from PIL import Image, ImageDraw


def train(name):
    img = Image.new('RGB', (280, 200), '#CCECFF')
    draw = ImageDraw.Draw(img)

    draw.rectangle((40, 110, 80, 150), '#C55A11')
    draw.polygon((40, 110, 60, 110 - 35, 80, 110), '#FFC000')

    draw.rectangle((80, 90, 160, 150), '#0070C0')
    draw.rectangle((160, 50, 240, 150), '#548235')
    draw.rectangle((150, 40, 250, 50), '#C55A11')
    draw.rectangle((185, 60, 215, 100), 'white')

    draw.rectangle((80, 60, 110, 90), 'red')
    draw.polygon((80, 60, 95, 60 - 26, 110, 60), '#FFC000')

    draw.ellipse((120, 130, 160, 170), 'black')
    draw.ellipse((180, 130, 220, 170), 'black')
    draw.ellipse((80, 140, 110, 170), 'black')

    img.save(name)
