from PIL import Image


def replace_color(image_path, output_path, from_color=(0, 0, 0), to_color=(255, 0, 0)):
    img = Image.open(image_path)
    img = img.convert('RGB')

    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            if pixels[i, j] == from_color:
                pixels[i, j] = to_color

    img.save(output_path)


s = input()

if s == 'red':
    replace_color('yandex_logo.png', 'ready.png', from_color=(0, 0, 0), to_color=(255, 0, 0))

elif s == 'black':
    replace_color('yandex_logo.png', 'ready.png', from_color=(255, 0, 0), to_color=(0, 0, 0))
