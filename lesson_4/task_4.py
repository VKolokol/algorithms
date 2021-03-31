"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_0():
    new_set = set(array)
    max_n = 1
    max_count = 1
    for el in new_set:
        count = array.count(el)
        if max_count < count:
            max_n = el
            max_count = count
    return f'Чаще всего встречается число {max_n}, ' \
           f'оно появилось в массиве {max_count} раз(а)'


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'



print(timeit("func_0()", globals=globals()))
print(timeit("func_1()", globals=globals()))
print(timeit("func_2()", globals=globals()))


"""
Сделал замеры и написал третий вариант. Ускорить получилось. Использовал перепод во множество, что уменьшило 
время ожидания результата почти в два раза.  Вывод времени представлен ниже:

func_0 : 2.1345146
func_1 : 4.3325741
func_2 : 4.4503053999999995
"""