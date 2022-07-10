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




class Bonus:
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

        return to_pay

    def give_bonus(self, bonus: Bonus):
        if bonus.__class__ in self.bonuses:
            self.bonuses[bonus.__class__] += bonus
        else:
            self.bonuses[bonus.__class__] = bonus


def test_perecent_bonus():
    b = PercentBonus(10)
    assert b.calculate(100) == 110


def test_add_bonuses_together():
    b1 = ValueBonus(100)
    b2 = ValueBonus(200)

    b3 = b1 + b2

    assert b3.value == 300
    assert isinstance(b3, ValueBonus)

    b1 = PercentBonus(10)
    b2 = PercentBonus(20)

    b3 = b1 + b2

    assert b3.value == 30
    assert isinstance(b3, PercentBonus)


# zdaj powyzszy test
# napisz analogiczny test dla PercentBonus
# coupling (sparowanie)
# cohesion (kohezja)
# SOLID
# https://www.youtube.com/results?search_query=arjan+codes


def test_add_value_bonus():
    # scenariusz ValueBonus
    b1 = ValueBonus(200)
    assert b1.value == 200

    e = PremiumEmployee(name="Jan Kowalski", rate_per_hour=100)
    e.register_time(5)
    e.give_bonus(b1)

    assert e.pay_salary() == (5 * 100) + 200


def test_add_percent_bonus():

    b2 = PercentBonus(10)
    e = PremiumEmployee(name="Jan Kowalski", rate_per_hour=100)
    e.register_time(5)
    e.give_bonus(b2)
    assert e.pay_salary() == (5 * 100) + (5 * 100) * 0.1


def test_add_value_and_percent_bonuses():
    # scenariusz 1
    b1 = ValueBonus(200)
    b2 = PercentBonus(10)
    e = PremiumEmployee(name="Jan Kowalski", rate_per_hour=100)
    e.register_time(5)
    e.give_bonus(b1)
    e.give_bonus(b2)
    assert e.pay_salary() == (5 * 100) + (5 * 100) * 0.1 + 200


def test_add_many_value_and_percent_bonusses():
    # kolejny scenariusz
    b1 = ValueBonus(200)
    b2 = PercentBonus(10)
    b3 = ValueBonus(300)
    b4 = PercentBonus(20)
    e = PremiumEmployee(name="Jan Kowalski", rate_per_hour=100)
    e.register_time(5)
    e.give_bonus(b1)
    e.give_bonus(b2)
    e.give_bonus(b3)
    e.give_bonus(b4)
    assert e.pay_salary() == (5 * 100) + (5 * 100) * 0.3 + 200 + 300
