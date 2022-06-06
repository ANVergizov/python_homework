from functools import wraps

def val_checker(function):
    def checker(func):
        @wraps(func)
        def wrapper(arg):
            if function(arg):
                res = func(arg)
            else:
                raise ValueError(f'wrong value! {arg}')
            return res
        return wrapper
    return checker


@val_checker(lambda x: x>0)
def calc_cube(x):
    return x ** 3

callback = calc_cube(6)
callback_2 = calc_cube(-3)

print(callback)
print(callback_2)
