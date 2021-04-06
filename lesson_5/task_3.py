"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""

from collections import deque
from timeit import timeit


def append_list():
    for el in range(100):
        a.append(el)


def append_deque():
    for el in range(100):
        b.append(el)


def insert_list():
    for el in range(100):
        a.insert(0, el)


def appendlef_deque():
    for el in range(100):
        b.appendleft(el)


def pop_list():
    for i in range(len(a)):
        a.pop(0)


def pop_deque():
    for i in range(len(b)):
        b.popleft()


a = []
b = deque([])



print(timeit("append_list()", globals=globals(), number=1000))
print(timeit("append_deque()", globals=globals(), number=1000))
print(timeit("insert_list()", globals=globals(), number=1000))
print(timeit("appendlef_deque()", globals=globals(), number=1000))
print(timeit("pop_list()", globals=globals(), number=1000))
print(timeit("pop_deque()", globals=globals(), number=1000))



'''За 1000 повторений получилось следующее время (1 - список, 2 - дек):
Добавление в конец
1. 0.005521999999999999
2. 0.005259100000000003
Добавление в начало
1. 7.6716472
2. 0.008316400000000002
Вырезать из начала
1. 3.7085264999999996
2. 0.009345599999999621


Как видно из замеров дек работает быстрее, разница довольно большая. Если добавление в конец остается
спорным вопросом. То все действия, производимые с первым элементом, однозначно быстрее - во много раз!
'''