import functools
import math
import operator


def factorial0(n):  # 4
    prod = 1
    for i in range(n):
        prod *= i + 1
    return prod


def factorial1(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod


def factorial2(n):
    return math.prod(range(1, n + 1))


def factorial3(n):
    return functools.reduce(operator.mul, range(1, n + 1), 1)


@functools.cache
def factorial4(n):
    if n == 0:
        return 1
    return factorial4(n - 1) * n


def test_factrial():
    funcs = [
        factorial0,
        factorial1,
        factorial2,
        factorial3,
        factorial4,
        math.factorial,
    ]

    for n in 0, 5, 100:
        for f in funcs:
            print(f"{f.__name__}({n})={f(n)}")


test_factrial()
