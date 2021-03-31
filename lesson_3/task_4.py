"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""

"""Скорее всего не так понял задание. Но как понял, так и сделал (собственно остальные также). 
Надеюсь механизм хотя бы немного верен..."""

import requests
import hashlib


cache = {"91fc1b3c6760efa86b88b462f1f0590b97151d876f264cb34c2671551ed5ac8f": 'тут должна быть структура html'}


class HabrPythonNews:

    def __init__(self, urls):
        self.urls = urls
        self.salt = str(len(urls))
        self.result = hashlib.sha256(self.salt.encode() + urls.encode()).hexdigest()
        self.check_url_in_cache(self.result)

    def check_url_in_cache(self, url):
        if cache.setdefault(url) is not None:
            print(cache[url])
        else:
            self.html = self.get_html(self.urls)
            cache[url] = self.html

    def get_html(self, site):
        try:
            result = requests.get(site)
            result.raise_for_status()
            return result.text
        except(requests.RequestException, ValueError):
            print('Server error')
            return False

    def __str__(self):
        return cache[self.result]


print(HabrPythonNews('https://ilibrary.ru/text/989/p.1/index.html'))  # Этого в кэше нет
d = HabrPythonNews('https://www.crummy.com/software/BeautifulSoup/')  # А этот есть
