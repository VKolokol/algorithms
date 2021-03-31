"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснвование рез-ам
"""
from timeit import timeit


i = 10
x = 100
y = 1000

def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


"""С использованием «Решета Эратосфена». Посмотрел 6 минутное видео одной учительницы по математике и вот
надумал такую реализацию"""
def simple_num(i):
    simple_nums = [2]
    n = 2
    while len(simple_nums) <= i:
        t = 0
        n += 1
        for el in simple_nums:
            if n % el == 0:
                t +=1
        if t == 0:
            simple_nums.append(n)
    return simple_nums[i - 1]


# print(simple(55))
print(simple_num(55))


# print("i = 10, number = 1000")
# print(timeit("simple(i)", globals=globals(), number=1000))
print(timeit("simple_num(i)", globals=globals(),number=10000))
#
# print("i = 100, number = 1000")
# print(timeit("simple(x)", globals=globals(), number=1000))
print(timeit("simple_num(x)", globals=globals(),number=10000))
#
# print("i = 1000, number = 1000")
# print(timeit("simple(y)", globals=globals(), number=1000))
# print(timeit("simple_num(y)", globals=globals(), number=1000))



"""
Последние замеры:
i = 10, number = 1000
0.09032200000000001
0.034700900000000034
i = 100, number = 1000
3.4640087
2.34939
i = 1000, number = 1000
727.7495921000001
180.85773159999997

Итог: через решето получается действительно быстрее. Однако время ожидания все равно очень большое.Первый алгоритм по
предварительной оценке соответсвует константе О(1) (по моему очень скромному мнению). Однако с ростом количества элементов 
сильно возрастает время ожидания. Получается , что О(1) проигрывает (в данном случае) О(n) (с решетом). 
"""