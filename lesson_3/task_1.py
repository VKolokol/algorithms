"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""


"""Для рассчетов были созданы 4 функции: для заполнения списка и словаря (2) и удаление данных из них (2).
Дополнительно была подключена библиотека timeit для более точно анализа времени"""

import timeit
import time


def profile(f):
    def g(n):
        start_time = time.time()
        value = f(n)
        end_time = time.time()
        return f'total time: {end_time - start_time}'

    return g


@profile
def add_to_list(n):
    for el in range(n):
        list_obj.append(el)
    return


@profile
def add_to_dict(n):
    for el in range(n):
        dict_obj[el] = el
    return


@profile
def del_el_in_list(n):
    for el in range(n):
        list_obj.pop()
    return


@profile
def del_el_in_dict(n):
    for el in range(n):
        dict_obj.popitem()
    return


dict_obj = {}
list_obj = []

count = 1000000

test_list = profile(add_to_list)
test_dict = profile(add_to_dict)

del_list = profile(del_el_in_list)
del_dict = profile(del_el_in_dict)

print('list ' + test_list(count))
print('dict ' + test_dict(count))

print('Del list ' + del_list(count))
print('Del dict ' + del_dict(count))

# ------------------------------------------------------------------------


code_to_test = """
def add_to_dict(n):
    for el in range(n):
        dict_obj[el] = el
    return

dict_obj = {}
count = 1000000
add_to_dict(count)
"""
code_to_test_2 = """
def add_to_list(n):
    for el in range(n):
        list_obj.append(el)
    return

list_obj = []
count = 1000000
add_to_list(count)
"""
elapsed_time = timeit.timeit(code_to_test, number=100) / 100
elapsed_time2 = timeit.timeit(code_to_test, number=100) / 100
print(f'create dict: {elapsed_time}\ncreate list: {elapsed_time2}')


"""Итог: последний запуск программы дал следующие результаты по времени - 
list total time: 0.07280611991882324
dict total time: 0.07380175590515137
Del list total time: 0.05588364601135254
Del dict total time: 0.07181024551391602
create dict: 0.079800137
create list: 0.079354941

Время заполнения списка и словаря практически одинаковое, что доказывает и одиночный запуск программы, 
и среднее значение за 100 итераций. А вот время изъятия элементов больше у словаря, 
что выглядит весьма интересно.
ПО О-большому .pop() для списка и .popitem() для словаря сложность одинаковая - О(1). Попытался найти причины,
ВОзможно это связано с тем, что алгоритмы popitem был изменен на новых версиях python.
И теперь 'забирает' элементы по принципу LIFO. """
