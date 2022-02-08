# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих
# типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H.
from abc import ABC, abstractmethod


class Cloth(ABC):
    def __init__(self, name=''):
        self.name = name

    @property
    def get_clothes(self):
        return 'Для пошива нужна ткань'

    @abstractmethod
    def some_abstract(self):
        return 'Умная мысль'


class Coat(Cloth):
    def __init__(self, name, size=0):
        super().__init__(name)
        self.size = size

    def get_clothes(self, **kwargs):
        result = (self.size / 6.5) + 0.5
        return result

    def some_abstract(self):
        return 'Встречают по одежке'


class Suit(Cloth):
    def __init__(self, name, hgth=0):
        super().__init__(name)
        self.hgth = hgth

    def get_clothes(self, **kwargs):
        result = 2 * self.hgth + 0.3
        return result

    def some_abstract(self):
        return ' - провожают по уму!'


coat_1 = Coat('Пальтишко серое', 44)
coat_2 = Coat('Tom Tailor', 42)
suit_1 = Suit('Большевичка темно-синий', 80)
print(coat_1.get_clothes())
print(coat_2.get_clothes())
print(suit_1.get_clothes())
print(coat_2.some_abstract())
print(suit_1.some_abstract())
