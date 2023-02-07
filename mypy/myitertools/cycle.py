import itertools


def cycle(iterable):
    saved = []
    for e in iterable:
        yield e
        saved.append(e)
    while saved:
        for e in saved:
            yield e


    saved = []
    while True:
        for e in iterable:
            saved.append(e)

for mycycle in cycle, itertools.cycle:
    print(mycycle)
    tab = (
        'Hello',
        [10, 20, 30],
        range(3),
        [e for e in range(3)],
        (e for e in range(3)),
        iter([10, 20, 30]),
        enumerate(range(3)),
    )
    for iterable in tab:
        print(list(itertools.islice(mycycle(iterable), 20)))

