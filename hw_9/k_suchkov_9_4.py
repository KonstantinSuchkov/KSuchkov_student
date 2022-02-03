# 4. Реализуйте базовый класс Car
class Car:
    speed = float
    color = str
    name = str
    is_police = None

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'машина {self.name} поехала.')

    def stop(self):
        print(f'машина {self.name} остановилась.')

    def turn(self, direction):
        if direction is None:
            return
        print(f'машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'скорость машины {self.name} - {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'скорость машины {self.name} - {self.speed}. Скорость превышена!')
        else:
            print(f'скорость машины {self.name} - {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'скорость машины {self.name} - {self.speed}. Скорость превышена!')
        else:
            print(f'скорость машины {self.name} - {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = True


lada = TownCar(70, 'баклажан', 'Лада седан', is_police=None)
gaz = WorkCar(50, 'капучино', 'Газель', is_police=None)
police = PoliceCar(100, 'синяя', 'opel', is_police=None)
lada.show_speed()
gaz.show_speed()
lada.go()
lada.turn(direction='налево')
lada.stop()
print(police.is_police)
