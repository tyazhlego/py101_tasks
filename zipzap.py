"""
Программа выводит на экран числа от 1 до 100 включительно, с новой строки.

Если число кратно трём, то вместо этого числа программа выводит слово "zip"
Если чисто кратно пяти, то вместо этого числа выводится слово "zap"
Если число кратно пятнадцати, то вместо этого числа выводится слово "zip-zap"

Тебе может понадобиться цикл for и ветвления
"""

for n in range(1, 101):
    if n % 15 == 0:
        print('zip-zap')
    elif n % 3 == 0:
        print('zip')
    elif n % 5 == 0:
        print('zap')
    else:
        print(n)