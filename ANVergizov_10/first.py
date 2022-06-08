matrix_1 = [[1, 2],
            [2, 1],
            [3, 2]]
matrix_2 = [[2, 3],
            [3, 2],
            [4, 5]]

class Matrix:

    def __init__(self, args):
        self.args = args

    def __str__(self):
        return '\n'.join(str(el) for el in self.args)

    def __add__(self, other):
        return Matrix([[x+y for x, y in zip(row_1, raw_2)]
                       for row_1, raw_2 in zip(self.args, other.args)])



m1 = Matrix(matrix_1)
print(m1)


m2 = Matrix(matrix_2)
print(m2)

m3 = m1 + m2
print(m3)