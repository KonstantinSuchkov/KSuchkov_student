# 2. Реализовать класс Road (дорога)

class Road:  # создаем класс и защищенные атрибуты
    _length = float
    _width = float

    def __init__(self, length=0, width=0):  # значения атрибутов передадим при создании экземпляра класса
        self._length = length
        self._width = width

    def get_materials(self):  # метод для расчета массы асфальта. 25 и 5 - масса асфальта для 1 м и толщина - из задания
        result = (self._length * self._width * 25 * 5) / 1000
        return print(f'{result} т')


example = Road(length=20, width=5000)
example.get_materials()
