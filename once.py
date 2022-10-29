from curses import nonl


def once(func):
    is_callable = True

    def inner(n):
        nonlocal is_callable
        if is_callable:
            is_callable = False
            return func(n)
        else:
            return

    return inner


@once
def double(n):
    return n * 2


# @once
def triple(n):
    return n * 3


# doubled_once = once(double)
# res = doubled_once(3)
# res2 = doubled_once(4)
res = double(2)
res2 = double(3)
print(res, res2)
