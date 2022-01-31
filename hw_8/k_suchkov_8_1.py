# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя
# пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
# выбросить исключение ValueError.

import re


# pattern = re.compile(r'(?P<username>\w+)@(?P<domain>\w+\.\w+)')

def email_parse(email_address):
    result = re.finditer(r'(?P<username>\w+.)@(?P<domain>\w+\.\w+)', email_address)
    for el in result:
        print(el.groupdict())
        break
    else:
        raise ValueError(f"wrong email: {email_address}")  # наверное есть более правильный способ для raise


email_parse('konstantinsuchkov@yandex.ru')
