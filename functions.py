"""Задания по ветвлениям, итерациям и вводу данных."""

# напиши функцию, которая принимает на вход любое
# количество чисел и сообщает, есть ли среди них чётное
def number(*args):
    a = 0
    for num in args:
        if num % 2 == 0:
            print('ЧЕТНОЕ ЕСТЬ!')
            break
        else:
            pass
number(1, 2, 3)


# используй тернарный оператор, чтобы вызвать функцию
# если возраст больше 21 года, в противном случае верни
# сообщение "Мы не продаём алкоголь несовершеннолетним."
def sell_alcohol(age):
    print('ПРОДАНО!')
age = 17
sell_alcohol(age) if age > 21 else print('Мы не продаём алкоголь несовершеннолетним.')


# напиши функцию, которая проверит, является ли строка ключевым словом в Питоне
# тебе понадобится модуль keyword, импортируй его и изучи с помощью dir()
import keyword
def check_keyword(input_line):
    print('Является keyword') if input_line in keyword.kwlist else print('Не является keyword')
check_keyword(input_line = input('Введите строку для проверки на keyword:\n'))


# напиши функцию, которая возвращает тип данных на русском языке:
# число, строка, булевый, None, список, кортеж, множество, словарь
# пример: get_type("что-то") возвращает "Это строка."
# пример2: get_type(42) возвращает "Это словарь."
def get_type(input_type):
    rus_type = type(input_type)
    if 'int' in str(rus_type) or 'long' in str(rus_type) or 'float' in str(rus_type) or 'complex' in str(rus_type):
        print('Это число')
    elif 'bool' in str(rus_type):
        print('Это булевое')
    elif 'str' in str(rus_type):
        print('Это строка')
    elif 'NoneType' in str(rus_type):
        print('Это None')
    elif 'list' in str(rus_type):
        print('Это список')
    elif 'tuple' in str(rus_type):
        print('Это кортеж')
    elif 'set' in str(rus_type):
        print('Это множество')
    elif 'dict' in str(rus_type):
        print('Это словарь')
    else:
        print('НЕИЗВЕСТНЫЙ ТИП')
input_type = None
get_type(input_type)