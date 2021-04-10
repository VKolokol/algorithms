"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile
import sys

sys.setrecursionlimit(5000)





@profile
def check_2(n):
    def check(i):
        if i == 1:
            return i
        else:
            return i + check(i - 1)
    return check(n)
print('Проверяем 1+2+...+n = n(n+1)/2, где n - любое натуральное число.')



k = 1000
#print(check_2(k))
print(check_2(k) == k*(k+1)/2)


"""
Если профилировать обычным способ, то таблицы появляются при каждом вызове функции. Решение:
Вызов функции с рекурсией внутри другой функции. 
Результат - одна таблица:

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    17     19.1 MiB     19.1 MiB           1   @profile
    18                                         def check_2(n):
    19     21.2 MiB      2.0 MiB        1001       def check(i):
    20     21.2 MiB      0.1 MiB        1000           if i == 1:
    21     21.2 MiB      0.0 MiB           1               return i
    22                                                 else:
    23     21.2 MiB      0.0 MiB         999               return i + check(i - 1)
    24     21.2 MiB      0.0 MiB           1       return check(n)


"""