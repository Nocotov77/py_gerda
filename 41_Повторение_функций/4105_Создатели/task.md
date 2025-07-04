# Создатели

* **Ограничение времени:** 1 секунда
* **Ограничение памяти:** 64Mb
* **Ввод:** стандартный ввод или `input.txt`
* **Вывод:** стандартный вывод или `output.txt`

– Так, а не создать ли нам новый мир? – спросил Аркканцлер, потирая руки. – Как раз есть немного времени перед завтраком.

Ну центральная звезда там точно должна быть, назовем ее оригинально – Солнце. Пусть там будет 9 планет, нет, пусть 8, до завтрака не успеть. Это такие большие камни, которые вертятся вокруг Солнца. Будет ли на них жизнь? Ну, это лишнее! Возись потом с ними, с живыми. Ладно, уговорили, но только на одной!

Так рассуждал Аркканцлер, создавая небольшой уютный мир быстренько, перед завтраком.

Напишите функцию `creators()`, которая получает один обязательный параметр – название звезды, остальные именованные со значениями по умолчанию:

*   `planets` – количество планет (по умолчанию 8);
*   `alive` – есть ли жизнь в системе (по умолчанию `True`).

Функция возвращает строковое значение в формате:

```
Система звезды {название}.
Количество планет: {количество}.
Жизнь есть!
```

Или

```
Жизни нет.
```

**Пример 1**

| Ввод                        | Вывод                                  |
| --------------------------- | -------------------------------------- |
| `print(creators('Солнце'))` | Система звезды Солнце.<br>Количество планет: 8.<br>Жизнь есть! |

**Пример 2**

| Ввод                              | Вывод                                  |
| --------------------------------- | -------------------------------------- |
| `print(creators('Бетельгейзе', 3, False))` | Система звезды Бетельгейзе.<br>Количество планет: 3.<br>Жизни нет. |