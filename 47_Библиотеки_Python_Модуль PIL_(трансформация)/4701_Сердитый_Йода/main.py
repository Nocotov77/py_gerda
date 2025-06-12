from PIL import Image


def apply_the_force(n, input_filename="yoda.png", output_filename="sense.png"):
    if n == 0:
        print("Ошибка: n не может быть равно нулю.")
        return

    try:
        image = Image.open(input_filename)
        image = image.convert("RGB")
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_filename}' не найден.")
        print("Убедитесь, что файл с изображением находится в той же папке, что и скрипт.")
        return

    width, height = image.size

    new_image = Image.new("RGB", (width, height))

    original_pixels = image.load()
    new_pixels = new_image.load()

    print("Применяю Силу... Идет обработка изображения.")

    for x in range(width):
        for y in range(height):
            r, g, b = original_pixels[x, y]

            max_diff = max(r, g, b) - min(r, g, b)

            delta = max_diff // n

            new_r = max(0, min(255, r + delta))
            new_g = max(0, min(255, g + delta))
            new_b = max(0, min(255, b + delta))

            new_pixels[x, y] = (new_r, new_g, new_b)

    new_image.save(output_filename)
    print(f"Готово! Преобразованное изображение сохранено в файл '{output_filename}'.")


if __name__ == "__main__":
    try:
        user_input = input("Силу чувствую я в тебе. Введи число n: ")
        n_value = int(user_input)
        apply_the_force(n_value)
    except ValueError:
        print("Ошибка: Введено не целое число. Перезапустите программу.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")