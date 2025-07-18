# К доске

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод или `input.txt`

**Вывод:** стандартный вывод или `output.txt`

В класс пришел новый учитель. Он пока не очень хорошо помнит фамилии учеников. В глобальной переменной `log` находится список учеников класса по журналу. Напишите функции:

*   `pupil_number(surname)` – если такой ученик есть в списке, функция выводит его номер, если нет, выводится сообщение:

    ```
    Такого ученика нет.
    ```

*   `add_pupil(surname)` – если такого ученика нет в журнале, функция добавляет ученика в журнал, причем он снова должен быть отсортирован по алфавиту, печатается сообщение:

    ```
    Ученик <фамилия> добавлен.
    ```

    Если такой ученик уже есть в журнале (считаем, что в нашем классе нет однофамильцев), печатается сообщение:

    ```
    Такой ученик уже есть в журнале.
    ```

*   `to_the_blackboard(n)` – вызывает ученика по номеру в журнале к доске и печатает сообщение:

    ```
    <Фамилия>, к доске!
    ```

    Два раза вызвать одного ученика нельзя. При повторном вызове выводится сообщение:

    ```
    Сан Саныч, Вы меня уже вызывали!
    ```

## Пример

**Ввод:**

```
log = ['Иванов', 'Кузнецов', 'Петрова']
pupil_number("Петрова")
add_pupil("Смирнов")
add_pupil("Иванов")
to_the_blackboard(4)
add_pupil("Васильев")
pupil_number("Смирнов")
to_the_blackboard(5)
```

**Вывод:**

```
3
Ученик Смирнов добавлен.
Такой ученик уже есть в журнале.
Смирнов, к доске!
Ученик Васильев добавлен.
5
Сан Саныч, Вы меня уже вызывали!