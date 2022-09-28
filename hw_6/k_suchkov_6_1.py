# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
# web-сервера nginx_logs.txt
file_1 = open('nginx_logs.txt', 'r', encoding='utf-8')
s = list(file_1)  # или file_1.readlines()
result = ()
my_list = []
for el in s:
    b = el.split('] "', )[1]  # находим нужные данные
    d = el.split(' /')[1]
    result = (el.split(' - - [')[0], b.split(' /')[0], d.split(' HTTP')[0])  # и заносим их в кортеж
    my_list.append(result)  # кортеж добавляем в список
# не понял почему, но если распечатать список через print, то не все выходит. Наверное какие-то ограничения в PyCharm
# по количеству строк.
for tple in range(len(my_list)):
    print(my_list[tple])
with open('list_log.txt', 'w') as file:  # проверил через запись в новый файл, вроде все правильно, количество записей
    print(*my_list, file=file, sep="\n")  # в списке (и данные) соответствует количеству записей в логе.
    # Проверял также через Excel

file_1.close()
