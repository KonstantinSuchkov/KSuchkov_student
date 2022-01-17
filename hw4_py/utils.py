from requests import get
from decimal import Decimal

response = get('http://www.cbr.ru/scripts/XML_daily.asp')

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
