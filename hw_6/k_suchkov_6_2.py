# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов
# из предыдущего задания.
from collections import Counter  # тк нельзя использовать обычный Count, то честно нашел в интернете Counter)


def get_spamer(list_for_search):
    dict_for_search = Counter(list_for_search)
    return dict_for_search.most_common(1)


def get_spamer_1(list_for_search):  # вариант решения через словари и max item
    dict_for_search = {}
    for log in list_for_search:
        dict_for_search[log] = dict_for_search.get(log, 0) + 1
    return max(dict_for_search.items(), key=lambda x: x[1])


file_1 = open('nginx_logs.txt', 'r', encoding='utf-8')
s = list(file_1)  # или file_1.readlines()
result = ()
my_list = []
for el in s:
    b = el.split('] "', )[1]  # находим нужные данные
    d = el.split(' /')[1]
    result = (el.split(' - - [')[0])  # и заносим их в кортеж
    my_list.append(result)
print(get_spamer(my_list))
print(get_spamer_1(my_list))
