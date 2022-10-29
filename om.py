def orwellian_math(func):
    def inner(*args, **kwargs):
        if args[0] == 2 and args[1] == 2:
            return func(2, 3)
        else:
            return func(*args)

    return inner


@orwellian_math
def add(a, b):
    return a + b


@orwellian_math
def addmore(a, b, c, d, e):
    return a + b + c + d + e


# print(orwellian_math(add)(2, 2))


# print(add(2, 2))
print(addmore(1, 2, 3, 4, 5))
