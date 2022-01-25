import sys

with open('hw_6/bakery.csv', 'r', encoding='utf-8') as file_1:  # открываем файл на чтение
    start_line = int(sys.argv[1]) if len(sys.argv) > 1 else 0  # определяем две переменные, которые будет вводить
    end_line = int(sys.argv[2]) if len(sys.argv) > 2 else 0  # пользователь через терминал - 1 и 2 значения после
    if start_line == 0:  # show_sales.py.
        for line in file_1:
            print(line)  # если пользователь не передал значений, то печатаем весь файл
    if start_line > 0 and end_line == 0:  # если значение только одно, то выводим срез от значения и дальше
        f = open('hw_6/bakery.csv', 'r', encoding='utf-8').readlines()
        print('\n'.join(f[start_line - 1:]))
    if end_line > 0:  # если даны два значения, то даем срез от 1 до 2
        f = open('hw_6/bakery.csv', 'r', encoding='utf-8').readlines()
        print('\n'.join(f[start_line - 1: end_line]))
file_1.close()
