# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
class Matrix:
    def __init__(self, some_list):
        self.some_list = some_list

    def __str__(self):
        for el in self.some_list:
            print('|', end=' ')
            for i in el:
                print(f'{i}', end=' ')
            print('|')
        return ''

    def __add__(self, other):
        res = self.some_list.copy()
        for i in range(len(self.some_list)):
            if len(self.some_list) != len(other.some_list):
                print(f'Ошибочка! Длины списков разные')
                exit(code=1)
            for j in range(len(self.some_list[i])):
                if len(self.some_list[i]) != len(other.some_list[i]):
                    print(f'Ошибочка! Длины списков разные')
                    exit(code=1)
                res[i][j] = self.some_list[i][j] + other.some_list[i][j]
        return res


a_list = [[31, 22], [37, 43], [51, 86], [3, 5, 32], [2, 4, 6], [-1, 64, -8], [3, 5, 8, 3], [8, 3, 7, 1]]
c_list = [[31, 22], [37, 43], [51, 86], [3, 5, 32], [2, 4, 6], [-1, 64, -8], [3, 5, 8, 3], [8, 3, 7, 1]]
b = Matrix(a_list)
d = Matrix(c_list)
print(b)
result_list = b + d
result = Matrix(result_list)
print(result)
