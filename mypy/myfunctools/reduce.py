import operator
import functools
import math


def reduce(f, iterable, initial=None):
    it = iter(iterable)
    if initial is None:
        res = next(it)
    else:
        res = initial
    for e in it:
        res = f(res, e)
    return res


values = [1000, 20, 30, 5, 5, 10]

print(reduce(operator.add, values))
print(sum(values))
print(reduce(operator.add, values, 0))
print(reduce(operator.mul, range(1, 6)))

print(reduce(operator.mul, [2] * 64))
print(2**64)
print(functools.reduce(operator.mul, [2] * 64))

print(reduce(operator.mul, values))
print(math.prod(values))
