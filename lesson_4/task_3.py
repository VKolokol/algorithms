"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""
from cProfile import run
from timeit import timeit

def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


string = 1233534

def main(s):
    revers_1(s)
    revers_2(s)
    revers_3(s)

print(revers_1(string))
print(revers_2(string))
print(revers_3(string))

print(timeit("revers_1(string)", globals=globals()))
print(timeit("revers_2(string)", globals=globals()))
print(timeit("revers_3(string)", globals=globals()))

run("revers_1(string)")
run("revers_2(string)")
run("revers_3(string)")

"""Вариант 3 лучше и быстрее. Самый простой в реализации, очень понятный и быстрый. 
Если можно сделать срез, лучше делать срез. Замеры времени через  timeit подтверждают мою мысль.
К сожалению, результаты тестирования через профайл показали нули, так как показывают только сотую долю секунды"""

