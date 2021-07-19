"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Подсказка:
Базовый случай здесь - угадали число или закончились попытки
"""

import random


def random_num(secret=random.randint(1, 100), n=10):
    answer = int(input('Number: '))
    if answer == secret:
        return 'You win!'
    if answer > secret:
        print('The secret number is less')
    if answer < secret:
        print('The secret number is greater')
    n -= 1
    if n < 1:
        return 'Yoy lose!'
    print(f'You have {n} attempts left')
    return random_num(secret, n)


print(random_num())
