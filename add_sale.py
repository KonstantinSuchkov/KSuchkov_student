import sys

with open('hw_6/bakery.csv', 'a+', encoding='utf-8') as file_2:  # открываем файл в режиме а+ для чтения и дозаписи
    price = sys.argv[1] if len(
        sys.argv) > 1 else '.'  # определяем, что price будет задаваться пользователем в терминале
    file_2.write(str(price) + '\n')  # а именно первым значением после 'add_sale.py'. Записываем цену в файл
file_2.close()
