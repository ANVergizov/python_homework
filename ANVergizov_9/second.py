class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def mass(self):
        self.mass = self._width * self._length * 25 * 5
        return self.mass



Nevskiy = Road(20, 5000)
print(Nevskiy.mass())