from abc import ABC, abstractmethod


class Employee:
    def __init__(self, name, rate_per_hour):
        self.name = name
        self.rate_per_hour = rate_per_hour
        self.worked_hours = 0

    def pay_salary(self):
        if self.worked_hours > 8:
            to_pay = (
                8 * self.rate_per_hour
                + (self.worked_hours - 8) * self.rate_per_hour * 2
            )
        else:
            to_pay = self.rate_per_hour * self.worked_hours
        self.worked_hours = 0
        return to_pay

    def register_time(self, hours):
        self.worked_hours = hours


class IBonus(ABC):
    @abstractmethod
    def calculate(self):
        pass


class Bonus(IBonus):
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.__class__(self.value + other.value)


class ValueBonus(Bonus):
    order = 2

    def calculate(self, to_pay: int):
        return to_pay + self.value


class PercentBonus(Bonus):
    order = 1

    def calculate(self, to_pay: int):
        return to_pay + (to_pay * self.value / 100)


class PremiumEmployee(Employee):
    def __init__(self, name, rate_per_hour):
        super().__init__(name, rate_per_hour)
        self.bonuses = {}

    def pay_salary(self):
        to_pay = super().pay_salary()

        for bonus in sorted(self.bonuses.values(), key=lambda x: x.order):
            to_pay = bonus.calculate(to_pay)
        self.bonuses = {}
        return to_pay

    def give_bonus(self, bonus: Bonus):
        if bonus.__class__ in self.bonuses:
            self.bonuses[bonus.__class__] += bonus
        else:
            self.bonuses[bonus.__class__] = bonus
