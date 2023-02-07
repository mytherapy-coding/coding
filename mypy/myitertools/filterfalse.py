import itertools


def filterfalse1(p, iterable):
    for e in iterable:
        if not p(e):
            yield e


def filterfalse2(p, iterable):
    return filter(lambda e: not p(e), iterable)


def even(x):
    return x % 2 == 0


values = [0, 1, 2, 5, 3, 4, 7, 12]

for filterfalse in itertools.filterfalse, filterfalse2, filterfalse1:
    print(list(filterfalse(even, values)))
