class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Car {self.name} {self.color} '

    def stop(self):
        return f'Car {self.name} {self.color} stop'

    def turn(self, direction):
        self.direction = direction
        return f'Car {self.name} {self.color} turn {self.direction}'

class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            print('Wow it is Dangerous!!')
        return self.speed

class WorkCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 40:
            print('Wow it is Dangerous!!')
        return self.speed

class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        return self.speed

class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        return self.speed


sport = SportCar(120, 'red', 'volga')
work = WorkCar(45, 'yellow', 'Jaguar')
police = PoliceCar(199, 'blue', 'UAZ')
town = TownCar(61, 'white', 'Cadillac')

print(sport.show_speed())
print(work.show_speed())
print(police.show_speed())
print(town.show_speed())
print(sport.go(), sport.turn('right'), sport.stop())