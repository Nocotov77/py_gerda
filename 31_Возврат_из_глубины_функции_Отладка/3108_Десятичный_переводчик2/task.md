# Десятичный переводчик-2

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод или `input.txt`

**Вывод:** стандартный вывод или `output.txt`

Усложним задачу.

Теперь нужно переводить число из системы счисления с основанием от 2 до 36! Вы же знаете, как образуются числа в 16-ричной системе счисления? Как только перестает хватать цифр от 0 до 9, начинают использоваться буквы латинского алфавита (мы будем использовать прописные) от A до F. По такому же принципу можно построить любую систему счисления, для которой хватит букв латинского алфавита: 26 букв + 10 цифр = 36!

Напишите функцию `decimal_translator_2(number, base)`, которая переводит целое число `number` из системы счисления с основанием `base` (от 2 до 36) в десятичную. Если это сделать невозможно, то функция должна не падать с ошибкой, а вернуть `None`.

**Пример 1**

| Ввод                        | Вывод |
|-----------------------------|-------|
| `print(decimal_translator_2("1Z", 36))` | 71    |

**Пример 2**

| Ввод                        | Вывод |
|-----------------------------|-------|
| `print(decimal_translator_2("1A0", 9))` | None  |

**Примечания**

В тестирующую систему сдайте только функцию, но не код, её вызывающий.