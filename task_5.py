"""
Задание 5.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""



class StackClass:
    def __init__(self):
        self.elems = []
        self.reserve_elems = []

    def is_empty(self):
        self.check_size()
        return self.elems == []

    def push_in(self, el):
        self.elems.append(el)

    def pop_out(self):
        self.check_size()
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        if len(self.elems) > 10:
            self.reserve()
        return len(self.elems)

    def reserve(self):
        while len(self.elems) != 10:
            self.reserve_elems.append(self.elems.pop())

    def reserve_size(self):
        return len(self.reserve_elems)

    def check_size(self):
        if self.elems == [] and self.reserve_elems != []:
            for i in range(len(self.reserve_elems)):
                self.elems.append(self.reserve_elems.pop())


if __name__ == '__main__':

    sc_obj = StackClass()

    print(sc_obj.is_empty())


    for el in range(20):
        sc_obj.push_in(el)

    print(sc_obj.stack_size())
    print(sc_obj.reserve_size())

    print(sc_obj.is_empty())

    full_stack = []

    for el in range(15):
        full_stack.append(sc_obj.pop_out())

    print(sc_obj.is_empty())

    print(full_stack)
    print(sc_obj.stack_size())
    print(sc_obj.reserve_size())