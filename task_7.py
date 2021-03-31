"""
Задание 7.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
"""
class DequeClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def add_to_front(self, elem):
        self.elems.append(elem)

    def add_to_rear(self, elem):
        self.elems.insert(0, elem)

    def remove_from_front(self):
        return self.elems.pop()

    def remove_from_rear(self):
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)



def pal_checker(string):
    dc_obj = DequeClass()

    for el in string:
        if el != ' ':   # Добавил проверку на пробелы и все работает. Возможно, я не правильно понял задание ...
            dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal

work_string = 'молоко делили ледоколом'
print(pal_checker(work_string))


# -------------------------------------------
# сли я неправильно понял, то вот сделал такой вариант...

"""def check_pol(string):
    output = string.split(' ')
    if len(output) > 1:
        string = ''.join(output)
    output = string[::-1]
    return output == string


work_string = 'молоко делили ледоколом'
my_string = 'довод'
print(check_pol(my_string))
print(check_pol(work_string))"""