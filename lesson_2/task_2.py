"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Используем операции % //, НЕ ИСПОЛЬЗУЕМ ОПЕРАЦИИ ВЗЯТИЯ ЭЛЕМЕНТА ПО ИНДЕКСУ

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""
import math as m


def count(num, i=0, even=0, uneven=0):
    rang = len(num) - i
    if rang == 0:
        return even, uneven
    if int(num) // m.pow(10, rang - 1) % 2 == 0:
        even += 1
    else:
        uneven += 1
    i += 1
    return count(num, i, even, uneven)


print(f'Количество четных и нечетных цифр в числе равно: {count(num=input("Введите число: "))}')
