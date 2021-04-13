"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random
from timeit import timeit


def merge_sort(alist, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(alist, start, mid)
        merge_sort(alist, mid, end)
        merge_list(alist, start, mid, end)
    return alist


def merge_list(alist, start, mid, end):
    left = alist[start:mid]
    right = alist[mid:end]
    k = start
    i = 0
    j = 0
    while start + i < mid and mid + j < end:
        if left[i] <= right[j]:
            alist[k] = left[i]
            i = i + 1
        else:
            alist[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            alist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            alist[k] = right[j]
            j = j + 1
            k = k + 1


n = int(input('Введите число элементов: '))
alist = [random.random()*random.randint(0, 49) for _ in range(n)]
print(f'Исходный - {alist}')
print(f'Отсортированный - {merge_sort(alist[:], 0, n)}')

# Замеры
"""alist = [random.random()*random.randint(0, 49) for _ in range(10)]
print(timeit('merge_sort(alist[:], 0, 10)',globals=globals(),number=1000))
alist = [random.random()*random.randint(0, 49) for _ in range(100)]
print(timeit('merge_sort(alist[:], 0, 100)',globals=globals(),number=1000))
alist = [random.random()*random.randint(0, 49) for _ in range(1000)]
print(timeit('merge_sort(alist[:], 0, 1000)',globals=globals(),number=1000))"""


# Итоги
"""
0.030747100000000138
0.2588908999999999
3.0932928000000004

Сортировка слиянием работает довольно быстро. Время выполнения её гораздо быстрее нежели пузырьком.
"""