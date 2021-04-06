"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit


def add_dict():
    for i in range(100):
        a[i] = i


def add_odict():
    for i in range(100):
        b[i] = i


def show_dict():
    for el in a.items():
        pass


def show_odict():
    for el in b.items():
        pass


def pop_dict():
    for i in range(len(a)):
        a.pop(i)


def pop_odict():
    for i in range(len(a)):
        b.pop(i)


a = {}
b = OrderedDict([])

print(timeit("add_dict()", globals=globals()))
print(timeit("add_odict()", globals=globals()))
print(timeit("show_dict()", globals=globals()))
print(timeit("show_odict()", globals=globals()))
print(timeit("pop_dict()", globals=globals()))
print(timeit("pop_odict()", globals=globals()))


''' Итог замеров (1. словарь обыкновенный (версия 3.9), 2. словарь orderdict)

Добавление элементов:
1. 6.7402521
2. 11.3680865
Все элементы (.items):
1. 7.8509788
2. 8.025067499999999
Удаление элементов:
1. 0.209508900000003
2. 0.278808699999999

Обычный словарь быстрее. Спасибо разработчикам за оптимизацию.
'''