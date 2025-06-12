from PIL import Image


def convert_to_grayscale(input_path, output_path, coef_r, coef_g, coef_b):
    img = Image.open(input_path)
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]

            gray = int(r * coef_r + g * coef_g + b * coef_b)

            gray = max(0, min(255, gray))

            pixels[i, j] = (gray, gray, gray)

    img.save(output_path)


try:
    input_path = "jellyfish.png"
    output_path = "gray_jelly.png"
    coef_r = float(input("Введите коэффициент для R: "))
    coef_g = float(input("Введите коэффициент для G: "))
    coef_b = float(input("Введите коэффициент для B: "))

    convert_to_grayscale(input_path, output_path, coef_r, coef_g, coef_b)
    print("Изображение преобразовано в оттенки серого и сохранено как 'jellyfish_grayscale.png'")
except Exception as e:
    print(f"Ошибка: {e}")
