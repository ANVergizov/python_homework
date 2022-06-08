from abc import ABC, abstractmethod

class Tex(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def formula(self):
        pass

class Coat(Tex):
    @property
    def formula(self):
        return self.param / 6.5 + 0.5

class Suit(Tex):
    @property
    def formula(self):
        return self.param * 2 * 0.3


a = Coat(67)
b = Suit(23)

print(a.formula)
print(b.formula)