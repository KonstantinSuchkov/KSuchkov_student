# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо
# только числами. Класс-исключение должен контролировать типы данных элементов списка.
class Error_no_digital(Exception):
    def __init__(self):
        self.numbers_list = []

    def input_numbers(self):
        while True:
            try:
                el = input('Введите число в список или stop для выхода: ')
                if el == 'stop' or el == 'STOP' or el == 'стоп':
                    break
                el = int(el)
                if type(el) is int:
                    self.numbers_list.append(el)
                    print(f'{self.numbers_list}')
            except Exception:
                print('Список принимает только числа!')


a = Error_no_digital()
print(a.input_numbers())
