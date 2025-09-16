import itertools


def starmap(f, iterable):
    for e in iterable:
        yield f(*e)


def starmap1(f, iterable):
    return (f(*e) for e in iterable)


values = [(2, 5), (3, 2), (10, 3)]

print(list(map(pow, [2, 3, 10], [5, 2, 3])))
print(list(map(pow, [e[0] for e in values], [e[1] for e in values])))


for mapper in itertools.starmap, starmap, starmap1:
    print(list(mapper(pow, values)))

nums = [-1, 3, 5, 10]

print([n**2 for n in nums])
print(list(map(pow, nums, itertools.repeat(2))))

for mapper in itertools.starmap, starmap, starmap1:
    print(list(mapper(pow, zip(nums, itertools.repeat(2)))))
