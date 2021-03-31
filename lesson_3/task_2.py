"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""
# sqlite, postgres, db_api, orm


from hashlib import pbkdf2_hmac
from binascii import hexlify


db = {
    'vlad': "b'3e97f9445244ea89624d1c52eef5a63df15b501e5aa16f6fbafa00034400672b'",
      'oleg777': "b'7b9269b199911ced37b0d1bc489111cc31fed17e58f3e26441a91219baf3b3b5'",
      'dora': "b'621a6b9b9073bbedde8914a4ee1c5e2bb37c6c0bedeb5cde9ad3c38c80e5bc4f'"
      }


class EnterInSystem():
    def __init__(self):
        self.login = input('Логин: ')
        self.salt = self.login.encode()
        self.passwd = input('Введите пароль: ').encode()
        self.passwd_check = input('Введите пароль еще раз для проверки: ').encode()
        self.check_passwd(self.passwd, self.passwd_check)

    def get_hash(self, pwd):
        obj = pbkdf2_hmac(hash_name='sha256',
                          password=pwd,
                          salt=self.salt,
                          iterations=100000)
        return hexlify(obj)

    def check_passwd(self, pwd, pwd_d):
        if self.get_hash(pwd) == self.get_hash(pwd_d):
            print('Вы ввели правильный пароль')
            self.check_in_db(self.login, self.get_hash(pwd_d))
        else:
            print('Пароль неверный, попробуйте еще!')
            EnterInSystem()

    def check_in_db(self, log, pwd):
        if str(pwd) == db.setdefault(log):
            print('Ты в системе! Рады тебя видеть!')
        else:
            print('О, а ты у нас впервые! Сохраним тебя, дружок-пирожок!')
            self.save_users(log, pwd)

    def save_users(self, login, passwd):
        db[login] = passwd


user = EnterInSystem()
