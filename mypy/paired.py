def paired1(iterable):
    prev_e = None
    for i, e in enumerate(iterable):
        print(i, e, i%2, prev_e)
        if i % 2 == 1:  # i - (i // 2) * 2
            yield prev_e, e
        prev_e = e


print(list(paired1([10,20,30,40,50,60])))


def paired2(iterable):
    it = iter(iterable)
    try:
        while True:
            yield next(it), next(it)
    except StopIteration:
        pass


print(list(paired2([10,20,30,40,50,60])))


def paired3(iterable):
    it = iter(iterable)
    try:
        for e in it:
            yield e, next(it)
    except StopIteration:
        pass


print(list(paired3([10,20,30,40,50,60])))


def paired4(iterable):
    pair = []
    for e in iterable:
        pair.append(e)
        if len(pair) == 2:
            yield tuple(pair)
            pair.clear()

print(list(paired4([10,20,30,40,50,60, 70])))


def paired5(iterable):
    it = iter(iterable)
    return ((e, next(it)) for e in it)


print(list(paired5([10,20,30,40,50,60])))

print('*********************')


def triple(iterable):
    it = iter(iterable)
    try:
        while True:
            yield next(it), next(it), next(it)
    except StopIteration:
        pass


print(list(triple(range(0, 100, 10))))


def tuple_k(k, iterable):
    t = []
    for e in iterable:
        t.append(e)
        if len(t) == k:
            yield tuple(t)
            t.clear()


print(list(tuple_k(2, [10,20,30,40,50,60])))
print(list(tuple_k(1, range(0, 100, 10))))


def tuple_k1(k, iterable):
    it = iter(iterable)
    try:
        while True:
            yield tuple([next(it) for _ in range(k)])
    except StopIteration:
        pass


print(list(tuple_k1(2, [10,20,30,40,50,60, 70])))
print(list(tuple_k1(3, range(0, 100, 10))))


