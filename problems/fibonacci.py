import functools


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


d = {}


# memoization

def fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in d:
        return d[n]
    d[n] = fib1(n - 1) + fib1(n - 2)
    return d[n]


@functools.cache
def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib2(n - 1) + fib2(n - 2)


def fib3(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f0 = 0
    f1 = 1
    for _ in range(2, n + 1):
        f2 = f0 + f1
        f0 = f1
        f1 = f2
    return f2


def fib4(n):
    f = [0, 1]
    for _ in range(2, n + 1):
        f.append(f[-1] + f[-2])
    return f[-1]


print(fib(30))
print(fib1(30))
print(fib2(30))
print(fib3(30))
print(fib4(30))
