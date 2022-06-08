class Cell:

    def __init__(self, num):
        if type(num) == int:
          self.num = num
        else:
            raise ValueError('It is not int type')

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num >= 0:
          return Cell(self.num - other.num)
        else:
            print('Число меньше нуля')

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __floordiv__(self, other):
        return Cell(self.num // other.num)

    def __truediv__(self, other):
        return Cell(self.num // other.num)

    def make_order(self, x):
        for _ in range(self.num // x):
            print('*' * x)
        return '*' * (self.num % x)


a = Cell(3)
b = Cell(34)
c = Cell(4)

print(f'{(a+b).num}\n {(a-c).num}\n {(a*b).num}\n {(a/b).num}\n {(a//c).num}\n ')
print(b.make_order(7))

