# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.
class Error_0(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return

    @staticmethod
    def get_divider(number=input('Ведите число: '), divider=input('Ведите число-делитель: ')):
        number = int(number)
        divider = int(divider)
        try:
            return number / divider
        except Exception:
            return f'нельзя делить на ноль!'


a = Error_0
print(a.get_divider())
# Ведите число: 100
# Ведите число-делитель: 0
# нельзя делить на ноль!
