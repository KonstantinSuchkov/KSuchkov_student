# 3. Написать декоратор для логирования типов позиционных аргументов функции.


def type_logger(func):
    def type_wrapper(*args):
        result = type(func(*args))
        print(f'{args[0]}: {result}')
        return result

    return type_wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
