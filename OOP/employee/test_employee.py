from employee import Employee, PremiumEmployee, ValueBonus, PercentBonus


def test_perecent_bonus():
    b = PercentBonus(10)
    assert b.calculate(100) == 110


def test_premium_eployee_overhours():
    e = PremiumEmployee(name="Jan Kowalski", rate_per_hour=100)
    e.register_time(10)
    assert e.pay_salary() == 1200


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
    assert e.pay_salary() == 0


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
