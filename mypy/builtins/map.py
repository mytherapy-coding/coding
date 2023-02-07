import itertools
import operator


def mymap(f, iterable):
    for e in iterable:
        yield f(e)


def mymap1(f, iterable):
    return [f(e) for e in iterable]


def mymap2(f, iterable):
    return (f(e) for e in iterable)


def mymap3(f, *iterables):
    for e in zip(*iterables):
        yield f(*e)


def mymap4(f, *iterables):
    return (f(*e) for e in zip(*iterables))


def mymap5(f, *iterables):
    return itertools.starmap(f, zip(*iterables))


def mymap6(f, iterable):
    it = iter(iterable)
    try:
        while True:
            yield f(next(it))
    except StopIteration:
        pass


def mymap7(f, iterable1, iterable2):
    it1 = iter(iterable1)
    it2 = iter(iterable2)
    try:
        while True:
            yield f(next(it1), next(it2))
    except StopIteration:
        pass


def mymap8(f, *iterables):
    iters = [iter(iterable) for iterable in iterables]
    try:
        while True:
            yield f(*[next(it) for it in iters])
    except StopIteration:
        pass


def square(x):
    return x ** 2


def prod(*elm):
    res = 1
    for e in elm:
        res *= e
    return res


values = [1, 2, 3, 2]

for mapper in map, mymap1, mymap2, mymap3, mymap4, mymap5, mymap6, mymap8:
    print(mapper)
    print(list(mapper(square, values)))
    print(list(mapper(lambda x: x ** 2, values)))
    print(list(mapper(int, mapper(str, values))))

print('**************************')
for mapper in map, mymap3, mymap4, mymap5, mymap8:
    print(mapper)
    print(list(mapper(operator.mul, values, values)))
    print(list(mapper(prod, values, values, values, values, values, values)))
    print(list(mapper(prod, values, values, values, values)))
