"""
Задание 6.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""


class QueueClass:
    def __init__(self):
        self.elems = []
        self.archive = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.check_task(item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

    def raise_archives(self):
        return self.archive.pop()

    def size_archive(self):
        return len(self.archive)

    def check_task(self, item):
        if item['status']:
            self.solved_problems(item)
        else:
            self.fix_status(item)

    def solved_problems(self, element):
        self.archive.insert(0, element)

    def fix_status(self, item):
        answer = input(f'Do you want to change your status - {item["name"]}? (Yes/No)')
        if answer.lower() == 'yes':
            self.archive.insert(0, item)
        else:
            self.elems.insert(0, item)

    def view_task(self, name):
        for char in self.elems:
            if name in char['name']:
                return f'{char["name"]}: {char["task"]}.'


if __name__ == '__main__':
    qc_obj = QueueClass()

    tasks_lst = [
                 {"name": 'Магазин', "task": 'Купить хлеб и молоко', "status": True},
                 {"name": 'Алгоритмы', "task": 'Сделать дз № 6', "status": False},
                 {"name": 'Mysql', "task": 'Сдать курсовую', "status": True},
                 {"name": 'Жизнь', "task": 'избавиться от мешков под глазами', "status": False}
                 ]

    for el in tasks_lst:
        qc_obj.to_queue(el)

    # print(qc_obj.view_task('Жизнь'))
