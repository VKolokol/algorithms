"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""


# Довольно похожая реализация (почти индентичная). Но разничца в том, что обработка идет через len(list).
# Его сложность по таблице O(len(...)). Однако если количество пользователей будет велико,
# то время поиска будет линейным, как и в примере ниже. Но наиболее время затратной является поиск на наличе
# элемента в наборе. Если набор пользователя будет велик и содержать множество значений,
# то время обработки будет сильно увеличено. В данном случае сложность будет O(N^2)


def chek_status_2(log, pwd):
    i = 0
    while i < len(db):  # --> O(len(...)) зависит от длины
        if log in db[i].values() and pwd in db[i].values(): # --> O(N^2)
            print(f'Welcome, {db[i]["name"]}')  # --> O(1)
            if db[i]['status'] is False:  # --> O(1)
                answer = input('You are not authorized.\nDo you want to be logged in? (Yes or No): ')  # --> O(1)
                if answer.capitalize() == 'Yes':  # --> O(len(...)) + O(1)
                    db[i]['status'] = True  # --> O(1)
                    return 'Great! Now you are with us!'  # --> O(1)
                else:
                    return f'Bye, {db[i]["name"]}!'  # --> O(1)
            else:
                return "You are logged in. Have a nice day!"  # --> O(1)
        i += 1


# Сложность по О-большому : O(N) - Линейное время исполнения. Итератор for - O(n), остальные О(1),
# кроме .capitalize - он зависит от длинны строки.


def check_status(log, pwd):
    for el in db:  # --> O(n)
        if log == el['login'] and pwd == el['password']:  # --> O(1)
            print(f'Welcome, {el["name"]}')  # --> O(1)
            if el['status'] is False:  # --> O(1)
                answer = input('You are not authorized.\nDo you want to be logged in? (Yes or No): ')  # --> O(1)
                if answer.capitalize() == 'Yes':  # --> O(len(...)) + O(1)
                    el['status'] = True  # --> O(1)
                    return 'Great! Now you are with us!'  # --> O(1)
                else:
                    return f'Bye, {el["name"]}!'  # --> O(1)
            else:
                return "You are logged in. Have a nice day!"  # --> O(1)
    return "User not found or incorrect data entered"  # --> O(1)


db = [
    {'login': 'bob777', 'password': 'qwerty33', 'name': 'Bob Smith', 'status': True},
    {'login': 'maryjane88', 'password': 'parker87', 'name': 'Mary Jane', 'status': True},
    {'login': 'batman', 'password': 'joker777', 'name': 'Bruce Wayne', 'status': False}
]

print('Welcome to Detroit!')
login = input('Enter login: ')
password = input('Enter password: ')

print(check_status(login, password))
print(chek_status_2(login,password))


""" Как итог написано две реализации практически индентичные, 
но в одной мы сравниваем конкретный элемент, 
а в другой проходимся по всем элементам дважды, что увеличивает время ожидания в 4 раза (N^2). 
Первый способ в данном случае побеждает (check_status)"""