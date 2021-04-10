"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from memory_profiler import profile
from collections import namedtuple
from recordclass import recordclass
from timeit import timeit
import numpy as np


# Заполнение списка элементами

@profile
def list_add(n):
    new_list = []
    for el in range(n):
        if el % 2 == 1:
            new_list.append(el)
    return


@profile
def my_gen(n):
    new_list = [el for el in range(n) if el % 2 == 1]
    return


# print(list_add(100000))
# print(my_gen(100000))

'''
    29     19.2 MiB     19.2 MiB           1   @profile()
    30                                         def list_add(n):
    31     19.2 MiB      0.0 MiB           1       new_list = []
    32     21.7 MiB      0.0 MiB      100001       for el in range(n):
    33     21.7 MiB      1.5 MiB      100000           if el % 2 == 1:
    34     21.7 MiB      1.0 MiB       50000               new_list.append(el)
    35     21.7 MiB      0.0 MiB           1       return
    
    
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    38     19.5 MiB     19.5 MiB           1   @profile()
    39                                         def my_gen(n):
    40     21.5 MiB      2.0 MiB      100003       new_list = [el for el in range(n) if el % 2 == 1]
    41     21.5 MiB      0.0 MiB           1       return
    
    
Реализовал добавление 100000 объектов в список. Полученные данные говорят о том, 
что незначительное преимущество имеет генератор. Если убрать декоратор из расчетов,
то на 0.5 MiB обычное добавление в список забирает памяти больше. 
В любом случае использование генератора эффективнее, он занимает гораздо меньше строк.
'''


# Задание 1 из урока 5
@profile
def company_1(n):
    for i in range(n):
        comp_name = f'Firma {i}'
        check_list = f'{i * 21} {i * 35} {i * 46} {i * 76}'.split()
        check_list = [int(el) for el in check_list]
        db[comp_name] = sum(Companies(check_list[0], check_list[1], check_list[2], check_list[3]))


Companies = namedtuple('Companies', ['q1', 'q2', 'q3', 'q4'])
db = {}

count = 10000


# print(company_1(count))
# print(timeit("company_1(count)", globals=globals(), number=1000))


@profile
def company_2(n):
    for i in range(n):
        comp_name = f'Firma {i}'
        check_list = list(map(int, f'{i * 21} {i * 35} {i * 46} {i * 76}'.split()))
        db_2[comp_name] = sum(Companies_2(check_list[0], check_list[1], check_list[2], check_list[3]))


Companies_2 = recordclass('Companies', ['q1', 'q2', 'q3', 'q4'])
db_2 = {}

# print(company_2(count))
# print(timeit("company_2(count)", globals=globals(), number=1000))

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    71     19.4 MiB     19.4 MiB           1   @profile()
    72                                         def company_1(n):
    73     20.9 MiB      0.3 MiB       10001       for i in range(n):
    74     20.9 MiB      0.0 MiB       10000           comp_name = f'Firma {i}'
    75     20.9 MiB      0.0 MiB       10000           check_list = f'{i*21} {i*35} {i*46} {i*76}'.split()
    76     20.9 MiB      0.6 MiB       70000           check_list = [int(el) for el in check_list]
    77     20.9 MiB      0.5 MiB       10000           db[comp_name] = sum(Companies(check_list[0], check_list[1], check_list[2], check_list[3]))



Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    87     20.9 MiB     20.9 MiB           1   @profile()
    88                                         def company_2(n):
    89     22.1 MiB      0.3 MiB       10001       for i in range(n):
    90     22.1 MiB      0.0 MiB       10000           comp_name = f'Firma {i}'
    91     22.1 MiB      0.6 MiB       10000           check_list = list(map(int,f'{i*21} {i*35} {i*46} {i*76}'.split()))
    92     22.1 MiB      0.3 MiB       10000           db_2[comp_name] = sum(Companies_2(check_list[0], check_list[1], check_list[2], check_list[3]))

Использование функции map() и библиотеки recordclass менее затратно по памяти нежели 
генератор+namedturple. Допольнительно произвел замеры времени:
18.8057387 - генератор+namedturple
17.6695044 - map() и recordclass
Соответственно по времени тоже победа map() и библиотеки recordclass.
"""


# list vs NumPy
@profile
def list_append():
    for el in range(100000):
        a.append(el)


@profile
def np_append():
    for el in range(100000):
        np.append(b, el)


a = []
b = np.array([])

# print(list_append())
print(np_append())

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   135     30.7 MiB     30.7 MiB           1   @profile()
   136                                         def list_append():
   137     34.5 MiB      0.0 MiB      100001       for el in range(100000):
   138     34.5 MiB      3.8 MiB      100000           a.append(el)

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   141     30.8 MiB     30.8 MiB           1   @profile()
   142                                         def np_append():
   143     30.8 MiB      0.0 MiB      100001       for el in range(100000):
   144     30.8 MiB      0.0 MiB      100000           np.append(b, el)

При добавлении элементов в массив (NumPy) память занимает только декаратор, в списках же ситуация иная. 
Одназначно, использования библиотеки NumPy спасает память от её заполнения.

"""
