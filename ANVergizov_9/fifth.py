class Stationery:

    def __init__(self, title,):
        self.title = title

    def draw(self):
        return 'Start drawing'

class Pen(Stationery):

    def draw(self):
        return 'Drawing by pen'

class Pencil(Stationery):

    def draw(self):
        return 'Drawing by pencil'

class Handle(Stationery):

    def draw(self):
        return 'Drawing by Handle'


pen = Pen('pen')
pencil = Pencil('pencil')
handle = Handle('handle')

print(pen.draw())
print(pencil.draw())
print(handle.draw())
