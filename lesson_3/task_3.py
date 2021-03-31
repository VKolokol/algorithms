"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

# hash?
list_obj = []
string = 'yaneponyal'   #здесь не очень понял, что делать надо ...
for i in range(len(string)):
    list_obj.append(hash(string[i]))
    list_obj.append(hash(string[i+1:]))
    list_obj.append(hash(string[:-(i+1)]))
    list_obj.append(hash(string[i+1:i+3]))

set_obj = {el for el in list_obj if el != 0}
print(f'Уникальных подстрок: {len(set_obj)}')