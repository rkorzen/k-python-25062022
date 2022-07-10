class Car:
    def __init__(self, name, engine_capacity, engine_type):

        self.name = name
        self.engine_capacity = engine_capacity
        self.engine_type = engine_type


class Engine:
    def __init__(self, engine_capacity, engine_type):
        self.engine_capacity = engine_capacity
        self.engine_type = engine_type


class Car:
    def __init__(self, name, engine: Engine):
        self.name = name
        self.engine = engine


class Bonus:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.__class__} v: {self.value}"

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


b1 = ValueBonus(100)
b2 = PercentBonus(10)

print(b1.order)
print(b2.order)

bonuses = [b1, b2]

print(bonuses)
print(sorted(bonuses, key=lambda x: x.order))

lista = ["a9", "c6", "b7"]


def second(x):
    return x[1]


# print(sorted(lista, key=lambda x: x[1]))
#
# print(sorted(lista, key=second))
#
#
# print(help(sorted))

bonuses = {}

bonuses[b1.__class__] = b1
bonuses[b2.__class__] = b2
print(bonuses)
b3 = PercentBonus(20)
bonuses[b3.__class__] += b3
print(bonuses)
