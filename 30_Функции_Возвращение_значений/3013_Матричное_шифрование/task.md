# Матричное шифрование

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод или `input.txt`

**Вывод:** стандартный вывод или `output.txt`

Этот способ шифрования основан на том, что текст можно записать в таблицу по строкам, а прочитать затем по столбцам. Не зная размеры таблицы, расшифровать его потом будет довольно сложно.

Напишите две функции – для шифрования `encrypt(text, n)` и для дешифровки – `decrypt(text, n)`. В первом случае функция принимает аргументы: текст для шифрования и размер строки в таблице, а возвращает зашифрованный текст. Второй функции для расшифровки кроме текста нужно передать размер строки исходной таблицы, а возвращает она расшифрованный текст.

Если длина текста не кратна числу `n`, то текст перед шифрованием дополняется пробелами до нужной длины, а после расшифровки лишние пробелы в конце удаляются.

## Пример 1

**Ввод**
```
from solution import *

print(encrypt('I love you!', 5))
print(decrypt('Ie!   ly oo vu ', 5))
```

**Вывод**
```
Ie!   ly oo vu 
I love you!
```

## Пример 2

**Ввод**
```
from solution import *

print(encrypt('Whirling, twirling round and round Falling softly to the ground.', 8))
print(decrypt('W,n nny h gadg git n  trrwrdFsoolio ao uirurlftnnlnolthdgiduile.', 8))
```

**Вывод**
```
W,n nny h gadg git n  trrwrdFsoolio ao uirurlftnnlnolthdgiduile.
Whirling, twirling round and round Falling softly to the ground.