name = input().strip()
dose = input().strip()
with open("recipe.txt", "w", encoding="utf-8") as f:
    f.write("Рецепт\n")
    f.write("Выписан " + name + "\n")
    f.write("Прописано: по " + dose + " касторки 3 раза в день.\n")
    f.write("Подпись: доктор Пилюлькин.")