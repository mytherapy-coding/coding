import itertools


def repeat(value, times=None):
    if times is None:
        while True:
            yield value
    else:
        for _ in range(times):
            yield value


print(list(repeat(-1, 9)))

print(list(zip(range(0, 100, 10), repeat(-1, 5))))

print(list(zip(range(10), repeat(-1, 5))) == list(zip(range(10), itertools.repeat(-1, 5))))
