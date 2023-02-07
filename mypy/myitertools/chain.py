import itertools


def chain1(*iterables):
    for iterable in iterables:
        for e in iterable:
            yield e


def chain2(*iterables):
    return (e for iterable in iterables for e in iterable)


for chain in chain1, chain2, itertools.chain:
    print(chain)

    tab = (
        ('Hello', ' ', 'World'),
        ([10, 20, 30], [4, 6, 8]),
        (range(3), range(2, -1, -1)),
        ([e for e in range(3)], [10, 30, 50]),
        ((e for e in range(3)), itertools.repeat(10, 5)),
        (iter([10, 20, 30]), reversed([10, 20, 30, 50])),
        (enumerate(range(0, 30, 10)), zip(range(3), 'Hello')),
    )

    for args in tab:
        print(f'{chain.__name__}{args}', ':', list(chain(*args)))
