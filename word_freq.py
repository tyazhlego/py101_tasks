"""
Программа считает Топ-100 слов для переданного ей текстого файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk

Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""

if __name__ == '__main__':
    pass

from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import string

def text_cleaner(path_to_file):
    with open(path_to_file, "r") as b:
        input_file = b.read()
    noneed_char = stopwords.words('english') + list(string.punctuation)
    need_char = [token for token in word_tokenize(input_file.lower()) if token not in noneed_char]
    final_list = (Counter(need_char).most_common(100))
    print(final_list)

text_cleaner(input('Введите путь до файла:\n'))