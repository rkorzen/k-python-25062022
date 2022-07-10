from abc import ABC, abstractmethod


class IBonus(ABC):
    @abstractmethod
    def calculate(self):
        pass


class BonusA(IBonus):
    def calculate(self):
        print("Calculate from BonusA")


a = IBonus()
b = BonusA()
