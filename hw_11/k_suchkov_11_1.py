# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год»
# . В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
import re


class Date:  # возможно не правильно понял задание, не понятно в каком виде дата должна изначально быть
    def __init__(self, date):  # def __init__(self, day=1, month=1, year=2000):
        self.date = date  # self.day = day self.month = month self.year = year

    def __str__(self):
        return self.date  # return f'{self.day}-{self.month}-{self.year}'

    @classmethod  # мне кажется classmethod здесь совсем не к месту, хотя может я просто не разобрался
    def get_date(cls, new_date):
        date_dict = re.finditer(r'(?P<day>\w+)-(?P<month>\w+)-(?P<year>\w+)', new_date)
        for el in date_dict:
            result = el.groupdict()
            day = int(result['day'])
            month = int(result['month'])
            year = int(result['year'])
            return day, month, year

    @staticmethod
    def get_valid(date):
        day = Date.get_date(date)[0]
        month = Date.get_date(date)[1]
        year = Date.get_date(date)[2]
        if day > 31:
            print(f'не может быть больше 31 дня!')
        elif month > 12:
            print(f'месяц не может быть больше 12!')
        elif year > 2022:
            print(f'может быть только текущий или прошедшие годы!')
        else:
            print('Все нормально!')


date1 = '26-03-2021'
my_date = Date('26-06-1986')
check_date = Date('11-11-2011')
print(my_date)
print(my_date.get_date('26-06-1986'))
for i in my_date.get_date('26-06-1986'):
    print(type(i))
Date.get_valid('26-55-2021')
Date.get_valid(date1)
