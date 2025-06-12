# Угадай слово

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод или `input.txt`

**Вывод:** стандартный вывод или `output.txt`

Напишите игру “Угадай слово” с компьютером. Игра заключается в следующем.

Вашей программе будет доступен файл `words.json`, в котором записан словарь: ключ – длина слова, значение – список английских слов (все буквы в нижнем регистре) с такой длиной. Там есть слова с длиной от 5 до 12 символов. Игроку даётся возможность набрать столько штрафных баллов, сколько букв в слове.

Начинаем играть.

1.  Игрок вводит число – длину слова.
2.  Компьютер выбирает из словаря случайное слово такой длины (пожалуйста, запишите это слово в переменную `word`!) и выводит его, закрывая буквы звездочками. И просит игрока ввести букву.
3.  Если пользователь ввёл не букву, вывести сообщение:

    ```
    Bad input. Try once more, please.
    ```

4.  Если такая буква есть в слове, компьютер выводит слово со всеми вхождениями этой буквы:

    ```
    Your word *****. Enter the letter.
    ```

5.  Если такой буквы нет, то выводится сообщение и штрафной счёт увеличивается на 1:

    ```
    There is no such letter in the word. Check is <check>.
    Your word **a**. Enter the letter.
    ```

6.  Если игрок угадал все буквы, выводится сообщение:

    ```
    You win! Your word is <WORD>.
    ```

7.  Если попытки кончились, а буквы отгаданы не все, выводится сообщение:

    ```
    You loss! Word was <WORD>.
    ```

Слово выводится в верхнем регистре.

**Пример игры:**

```
5
Your word *****. Enter the letter.
a
Your word **a**. Enter the letter.
e
There is no such letter in the word. Check is 1.
Your word **a**. Enter the letter.
i
There is no such letter in the word. Check is 2.
Your word **a**. Enter the letter.
o
There is no such letter in the word. Check is 3.
Your word **a**. Enter the letter.
n
Your word **an*. Enter the letter.
t
Your word t*an*. Enter the letter.
r
There is no such letter in the word. Check is 4.
Your word t*an*. Enter the letter.
h
Your word than*. Enter the letter.
k
You win! Your word is THANK.