"""
2.*	Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

1. вариант
defaultdict(list)
int(, 16)
reduce

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
"""
from collections import defaultdict


class HexNumber:
    def __init__(self, num):
        self.num = num
        self.def_dict = defaultdict(list)

    def create_list(self, item):
        self.item = str(hex(item))
        self.def_dict[item] = [el.upper() for el in self.item if el not in '0x']
        return self.def_dict[item]

    def __add__(self, other):
        self.result = self.num + other.num
        return self.create_list(self.result)

    def __mul__(self, other):
        self.result = self.num * other.num
        return self.create_list(self.result)


num_1 = int(input('Введите число в 16-ричной системе счистления: '), 16)
num_2 = int(input('Введите число в 16-ричной системе счистления: '), 16)
a = HexNumber(num_1)
b = HexNumber(num_2)
print(f'Сумма чисел из примера: {a + b}')
print(f'Произведение чисел из примера: {a * b}')
