from functools import wraps

def type_logger(func):
    def wrapper(arg):
        res = func(arg)
        print(f'{func.__name__} type argument {arg} is {type(arg)}')
        return res
    return wrapper



@type_logger
def calc_cube(x):
    return x ** 3

cube = calc_cube(5)
print(cube)