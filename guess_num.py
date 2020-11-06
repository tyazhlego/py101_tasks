"""
Программа генерирует число от 0 до 1_000_000 и предлагает угадать его.

Программа должна приветствовать пользователя и считывать число с клавиатуры
Если число меньше загаданного, то программа выводит сообщение о том, что число
меньше
Если больше загаданного, то программа выводит сообщение о том, что больше

Программа должна выводить сообщения-предупреждения, если:
* пользователь ввёл не число
* число не входит в обозначенный в условии диапазон
Если пользователь ничего не ввёл/ввёл "exit", то происходит выход из программы.

Тебе может понадобится модуль random, цикл while и ветвления
"""

import random
guess_number = random.randint(0, 1000000)
print(guess_number)
input_number = input('Привет! Попробуй угадать число от 0 до 1млн:\n')
while guess_number != input_number:
    if 'exit' in input_number:
        break
    elif int(input_number.isdigit()) == 0 :
        input_number = input('Введите число! Попробуй еще:\n')
    elif int(input_number) > 1000000 or int(input_number) < 0 :
            input_number = input('Диапазон числа от 0 до 1млн! Попробуй еще:\n')
    elif int(input_number) > guess_number:
        input_number = input('Загаданное число меньше! Попробуй еще:\n')
    elif int(input_number) < guess_number:
            input_number = input('Загаданное число больше! Попробуй еще:\n')
    else:
        print('Вы угадали! Заберите приз по ссылке: clck.ru/Rnw7n')
        break