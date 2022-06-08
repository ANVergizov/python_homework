class Worker:
    def __init__(self, name, surname, position, wage, bonus):
      self.name = name
      self.surname = surname
      self.position = position
      self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'Full name of worker is {self.name} {self.surname}'
    def get_income(self):
        return f'Full income of worker is {sum(self._income.values())} {self._income}'


worker = Position('Joe', 'Tribianni', 'Actor', 10000, 2000)

print(f'{worker.get_full_name()}\n {worker.get_income()}')