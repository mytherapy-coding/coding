import itertools


def myfilter(p, iterable):
    for e in iterable:
        if p(e):
            yield e


def myfilter1(p, iterrable):
    return (e for e in iterrable if p(e))


def even(x):
    return x % 2 == 0


values = [0, 1, 2, 5, 3, 4, 7, 12]

for filter_all in filter, myfilter, myfilter1:
    print(list(filter_all(even, values)))
