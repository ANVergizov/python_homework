from time import sleep

class Lighter:
    __color = ['red', 'yellow', 'green']

    def running(self):
        print(self.__color[0])
        sleep(7)
        print(self.__color[1])
        sleep(2)
        print(self.__color[2])
        sleep(1)
        return 'lighter end work'


light = Lighter()
print(light.running())
