# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский

def num_translate(number):
    """number - число от 0 до 10 на английском"""
    numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
               'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    print(f'"' + numbers[number] + '"')
    # return numbers[number] - если не надо print, не совсем понял по заданию


num_translate("zero")
