# 6. Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом
# командной строки: для записи данных и для вывода на экран записанных данных. При записи передавать из командной строки
# значение суммы продаж
def show_sales(start_line=0, end_line=0):
    with open('bakery.csv', 'r', encoding='utf-8') as file_1:
        if start_line == 0:
            for line in file_1:
                print(line)
        if start_line > 0 and end_line == 0:
            f = open('bakery.csv', 'r', encoding='utf-8').readlines()
            print('\n'.join(f[start_line - 1:]))
        if end_line > 0:
            f = open('bakery.csv', 'r', encoding='utf-8').readlines()
            print('\n'.join(f[start_line - 1: end_line]))


def add_sale(price):
    with open('bakery.csv', 'a+', encoding='utf-8') as file_2:
        file_2.write(str(price) + '\n')


# т.к. у меня не получалось запустить через консоль, я реализовал функции. Файлы add_sale.py и show_sales.py
# запустил через терминал, вроде все сработало.

add_sale(5978.5)
add_sale(8914.3)
add_sale(7879.1)
add_sale(1573.7)
show_sales()
show_sales(3)
show_sales(1, 3)
