# 3. Реализовать базовый класс Worker (работник)
class Worker:
    name = str
    surname = str
    position = str
    _income = {'wage': 0, 'bonus': 0}

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    @property
    def income(self):
        return self._income


class Position(Worker):
    def __init__(self, name, surname, position=None, income=None):
        super().__init__(name, surname, position, income)
        if income and position is None:
            return

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        result = self._income['wage'] + self._income['bonus']
        print(result)


amelia = Position('Amelia', 'Suchkova', 'child', income={'wage': 5000, 'bonus': 150})


print(amelia.name, amelia.surname, amelia.position, amelia.income)
amelia.get_full_name()
amelia.get_total_income()
