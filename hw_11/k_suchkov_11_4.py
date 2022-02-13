# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).
store_moscow = {}  # в идеале нужно было бы сделать один общий словарь с вложенными списками, но я слишком далеко
store_perm = {}  # зашел и не хватило времени переделывать, а очень жаль, ведь код можно сократить и улучшить.


class Warehouse:  # класс склад с параметром адрес

    def __init__(self, store_adress):
        self.store_adress = store_adress


class Equipment_office(Warehouse):  # класс оргтехника наследуют от склада и имеет свои параметры:
    global store_perm
    global store_moscow

    def __init__(self, store_adress, name, price, amount):  # наименование, цена, количество(amount)
        # эти параметры характерны для всей оргтехники
        super().__init__(store_adress)
        self.name = name
        self.price = price
        self.amount = amount
        if store_adress == 'Moscow':
            store_moscow[self.name] = self.amount
        if store_adress == 'Perm':
            store_perm[self.name] = self.amount

    def arrival_eqiup(self, quantity):  # метод прихода техники

        self.amount = self.amount + quantity
        if self.store_adress == 'Moscow':
            store_moscow[self.name] = self.amount
            return f'на складе: {self.store_adress} - техника {store_moscow}'
        if self.store_adress == 'Perm':
            store_perm[self.name] = self.amount
            return f'на складе: {self.store_adress} - техника: {store_perm}'

    def move_store(self, quantity, store_to):  # метод отправки техники с одного склада на другой
        global store_perm
        global store_moscow
        if self.store_adress == 'Moscow' and store_to == 'Perm':
            store_moscow[self.name] -= quantity
            store_perm[self.name] += quantity
            return f'на складе: {self.store_adress} - техника: {store_moscow}, ' \
                   f'на складе: {store_to} - техника: {store_perm}'
        if self.store_adress == 'Perm' and store_to == 'Moscow':
            store_perm[self.name] -= quantity
            store_moscow[self.name] += quantity
            return f'на складе: {self.store_adress} - техника: {store_perm}, ' \
                   f'на складе: {store_to} - техника: {store_moscow}'


class Printer(Equipment_office):  # отдельные типы оргехники со своими уникальными параметрами
    def __init__(self, store_adress, name, price, amount, laser=True):
        super().__init__(store_adress, name, price, amount)
        self.laser = laser
        if self.store_adress == 'Moscow':
            store_perm[name] = 0
        if self.store_adress == 'Perm':
            store_moscow[name] = 0


class Scanner(Equipment_office):
    def __init__(self, store_adress, name, price, amount, param):
        super().__init__(store_adress, name, price, amount)
        self.param = param
        if self.store_adress == 'Moscow':
            store_perm[name] = 0
        if self.store_adress == 'Perm':
            store_moscow[name] = 0


class Xerox(Equipment_office):
    def __init__(self, store_adress, name, price, amount, param):
        super().__init__(store_adress, name, price, amount)
        self.param = param
        if self.store_adress == 'Moscow':
            store_perm[name] = 0
        if self.store_adress == 'Perm':
            store_moscow[name] = 0


# Task 4
hp_printer = Printer(store_adress='Moscow', name='Printer HP', price=10000, amount=50, laser=True)
print(hp_printer.name, hp_printer.price, hp_printer.store_adress, hp_printer.laser)
port_scaner = Scanner(store_adress='Perm', name='Scanner L2F', price=5600, amount=20, param='Portable')
print(port_scaner.name, port_scaner.price, port_scaner.store_adress, port_scaner.param)

# Task 5
print(hp_printer.amount)
print(hp_printer.arrival_eqiup(10))  # на склад в Москве пришли 10 принтеров
print(hp_printer.arrival_eqiup(-10))  # продали 10 принтеров со склада в Москве
print(hp_printer.move_store(10, 'Perm'))  # отправляем с Москвы в Пермь 10 принтеров
print(port_scaner.move_store(5, 'Moscow'))  # а теперь отправим сканеры с Перми в Москву (там вообще не было сканеров)
some_xerox = Xerox(store_adress='Moscow', name='Super Xerox', price=10000, amount=22, param='cool')  # нашли 22 ксерокса
print(some_xerox.move_store(15, 'Perm'))  # отправили 15 ксероксов в москву
