# Реализовать базовый класс Worker (работник),
# в котором определить публичные атрибуты name, surname, position (должность),
# и защищенный атрибут income (доход). Последний атрибут должен ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
#
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
#
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).
#
# П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
# str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.

class Worker:
    def __init__(self, name, surname, position, wage):
        self.wage = wage
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": wage * 0.5}


class Position(Worker):

    def get_full_name(self):
        print(f'{self.name} , {self.surname} {self.position}')

    def get_total_income(self):
        print(f'{int(self._income["bonus"]), self._income["wage"]}')


worker3 = Position('Иванов', 'Ивановича', 'зам директор', 6000)
worker3.get_full_name()
worker3.get_total_income()
