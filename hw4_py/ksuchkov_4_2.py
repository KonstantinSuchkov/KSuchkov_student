# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests
from requests import get
from decimal import Decimal  # в задании буду использовать Decimal, тк иначе значение функция возвращала в

# виде str, а преобразовать в float у меня не получилось (valueerror could not convert string to float python)
#

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
print(response.status_code)

content = response.content.decode(encoding=response.encoding)


def currency_rates(valute):
    """
     valute - указывается код валюты в кавычках и верхним регистром, например: 'USD'
    """
    for el in content.split(valute)[1:]:
        result = el.split('Value>')[1]
        result = result.split('</')[0]
        val = result.replace(',', '.')
        val = Decimal(val)
        return val


print(currency_rates('USD'))
print(type(currency_rates('USD')))
print(currency_rates('EUR'))
print(currency_rates('SOMEVALUTE'))  # проверяем на несуществующую валюту, ответ None
print(currency_rates('USD') + currency_rates('EUR'))  # проверка на математику