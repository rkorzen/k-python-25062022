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


class ValueBonus(Bonus):
    pass


class PercentBonus(Bonus):
    pass


class PremiumEmployee(Employee):
    def pay_salary(self):
        to_pay = super().pay_salary()
        to_pay += self.bonus.value
        return to_pay

    def give_bonus(self, bonus: Bonus):
        self.bonus = bonus


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


def add_value_and_percent_bonuses():
    # scenariusz 1
    b1 = ValueBonus(200)
    b2 = PercentBonus(10)
    e = PremiumEmployee(name="Jan Kowalski", rate_per_hour=100)
    e.register_time(5)
    e.give_bonus(b1)
    e.give_bonus(b2)
    assert e.pay_salary() == (5 * 100) + (5 * 100) * 0.1 + 200


def add_many_value_and_percent_bonusses():
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
