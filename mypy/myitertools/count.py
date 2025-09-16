import itertools


def count(start=0, step=1):
    while True:
        yield start
        start += step


print(list(zip(range(3), count(20))))
print(list(itertools.islice(count(20, 0), 4)))

print(list(zip(range(3), itertools.count(20))))
print(list(itertools.islice(itertools.count(20, 0), 4)))
