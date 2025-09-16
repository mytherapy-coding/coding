import itertools
import operator


def gen_sum(iterable):
    it = iter(iterable)
    res = next(it)
    yield res
    for e in it:
        res = operator.add(res, e)
        yield res


def gen_prod(iterable):
    it = iter(iterable)
    res = next(it)
    yield res
    for e in it:
        res = operator.mul(res, e)
        yield res


def gen_min(iterable):
    it = iter(iterable)
    res = next(it)
    yield res
    for e in it:
        res = min(res, e)
        yield res


def accumulate(iterable, f=operator.add, *, initial=None):
    it = iter(iterable)
    if initial is None:
        try:
            res = next(it)
        except StopIteration:
            return
    else:
        res = initial
    yield res
    for e in it:
        res = f(res, e)
        yield res


values = [10, 20, 30, 5, 5, 10]
print(list(gen_sum(values)))
print(list(gen_prod(values)))
print(list(gen_min(values)))

for acc in accumulate, itertools.accumulate:
    print(acc)
    print(list(acc(values, operator.add)))
    print(list(acc(values, operator.mul)))
    print(list(acc(values, min)))
    print(
        list(
            acc(
                [],
                min,
            )
        )
    )
    print(list(acc([], min, initial=0)))
    print(list(acc(values, operator.add, initial=1000)))
    print(list(acc(values)))
