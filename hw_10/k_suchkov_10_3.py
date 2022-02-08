# 3. Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка».
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны
# быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение
# (__mul__()), деление (__floordiv__, __truediv__()).
class Cell:
    def __init__(self, param):
        self.param = int(param)  # количество ячеек в клетке Cell, целое число

    def __add__(self, other):  # сложение клеток
        return self.param + other.param

    def __sub__(self, other):  # вычитание
        return self.param - other.param if 0 < self.param - other.param else 'Не может быть минус ячеек!'

    def __mul__(self, other):  # умножение
        return self.param * other.param

    def __truediv__(self, other):  # деление
        return self.param // self.param

    def make_order(self, number):
        for el in range(self.param // number):
            print(f'*' * number)
        if self.param - (self.param // number * number) > 0:
            print(f'*' * (self.param - (self.param // number * number)))
        return ''


cell_alpha = Cell(param=40)
cell_beta = Cell(param=30)
print(cell_beta + cell_alpha)
print(cell_beta - cell_alpha)
print(cell_alpha * cell_beta)
print(cell_alpha / cell_beta)
print(cell_beta.make_order(7))
