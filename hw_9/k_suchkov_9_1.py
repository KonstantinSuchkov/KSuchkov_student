# 1. Создать класс TrafficLight (светофор)
import time


class TrafficLight:
    __color = ['красный', 'жёлтый', 'зелёный']

    def running(self):
        print(f'Стой! Светофор {self.__color[0]}')
        time.sleep(7)
        print(f'Приготовься! Светофор {self.__color[1]}')
        time.sleep(2)
        print(f'Иди! Светофор {self.__color[2]}')
        time.sleep(3)


check_exem = TrafficLight()
check_exem.running()
