# Загадка-2

Ограничение времени 1 секунда

Ограничение памяти 64Mb

Ввод стандартный ввод или input.txt

Вывод стандартный вывод или output.txt


Теперь так легко обмануть компьютер не удастся, нужно придумать, как получить подсказку, не используя команду  print. Сдайте в тестирующую систему одну строку, которую нужно записать в указанное место, чтобы получить подсказку. Помните,  print использовать нельзя!

Код программы:
```python
import random  
  
months = ["январь", "февраль", "март", "апрель",  
"май", "июнь", "июль", "август", "сентябрь",  
"октябрь", "ноябрь", "декабрь"]  
secret = random.choice(months)  
# ВЫШЕ НЕПОНЯТНЫЙ КОД!  
# сейчас в переменной secret лежит загаданный месяц  
message = "Нельзя использовать лишний print!"  
### В следующую строку нужно записать решение!  
  
### В предыдущую строку нужно записать решение!  
print(message)  
print("Какой месяц я загадал?")  
solution = input()  
# НИЖЕ НЕПОНЯТНЫЙ КОД!  
# тут программа проверяет, совпал ли ответ с загаданным словом  
if secret == solution:  
print("Точно!")  
elif solution not in months:  
print("Это слово вообще не месяц!")  
else:  
print("Не угадал!")  
 ```

В тестирующую систему сдайте только одну строку!