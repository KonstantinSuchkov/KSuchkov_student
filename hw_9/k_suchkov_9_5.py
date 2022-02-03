# 5. Реализовать класс Stationery (канцелярская принадлежность)
class Stationery:
    title: str

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        super().__init__()
        self.title = 'ручка'

    def draw(self):
        print(f'{self.title.title()}, начинаем делать запись')


class Pencil(Stationery):
    def __init__(self):
        super().__init__()
        self.title = 'карандаш'

    def draw(self):
        print(f'{self.title.title()}, будем рисовать эскиз')


class Handle:
    def __init__(self):
        super().__init__()
        self.title = 'маркер'

    def draw(self):
        print(f'{self.title.title()}, выделим в тексте основные понятия')


pen = Pen()
pencil = Pencil()
handle = Handle()
pen.draw()
pencil.draw()
handle.draw()
